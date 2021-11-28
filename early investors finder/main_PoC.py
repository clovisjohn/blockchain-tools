import requests
import json
import web3

#Uniswap subgraph query format
"""{
    swaps(orderBy: timestamp, orderDirection: asc, first:1000,skip:0, where:
    { pair: "0xf82d8ec196fb0d56c6b82a8b1870f09502a49f88", amount0Out_not:0, timestamp_gt:0  }
    ) {	
    id
        to
    		timestamp
    }
    }"""


def query_builder(last_tstamp,pair):
    '''
    take as input a token address
    return a query made suing this address
    '''
    return """{
    swaps(orderBy: timestamp, orderDirection: asc, first:1000, where:
    { pair: \"""" +  pair + """", amount0Out_not:0,timestamp_gt: """ +  str(last_tstamp) + """ }
    ) {	
        to
        timestamp
    }
    }"""
    
def query_builder2(last_tstamp,pair):
    '''
    take as input a token address
    return a query made suing this address
    '''
    return """{
    swaps(orderBy: timestamp, orderDirection: asc, first:1000, where:
    { token0: \"""" +  pair + """",timestamp_gt: """ +  str(last_tstamp) + """ }
    ) {	
        origin
        timestamp
    }
    }"""


def query_graph(query, endpoint):
    '''
input: valid uniswap graphql query
output: api response as a dictionary
    '''
    
    r = requests.post(endpoint, json={"query": query})
    if r.status_code == 200:
        parsed_json = json.loads(r.text)
        return parsed_json
    else:
        raise Exception("Query failed to run with a {r.status_code}.")

def get_first_investors_list(bundle, size):

    
    '''
    pair: pair addy
    size: size*1000 = amount of addys to scrape(duplicates included)
    '''
    pair=bundle[0]
    dex=bundle[1]
    keyword='to'
    if dex=='uniswap-v2':
        endpoint="https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2"
    elif dex=='uniswap-v3':
        endpoint="https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v3"
        keyword='origin'
    elif dex=='sushiswap':
        endpoint='https://api.thegraph.com/subgraphs/name/sushiswap/exchange'
    
    l=[] #dummy list to store swaps data
    k=[0,1] #list of timestamp 
    while len(k)<=size:                          # len(k)*1000 = scraped addys (duplicate included)
        if dex=='uniswap-v3' :
            t_query=query_builder2(k[-1],pair)  #build a valid uniswap query to retrieve a swaps list from uniswap subgraph
        else:
            t_query=query_builder(k[-1],pair)
        temp=query_graph(t_query,endpoint)     #use the previous query to make an api request
        l=l + temp["data"]["swaps"]
        try:
            last_tstamp=temp["data"]["swaps"][-1]["timestamp"] #get time_stamp of the last element of the generated swaps list
        except IndexError:
            break
        k.append(last_tstamp)                     #add the last timestamp to the list of timestamp
    
    f=[i["to"] for i in l] #extract addys from the dummy list
  
    return list(dict.fromkeys(f))

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

def is_contract(addy): #check if the address provided is a contract address
    '''
    input: ethereum address 0x...
    return: boolean
    '''
    global project_id
    w3 = web3.Web3(web3.Web3.HTTPProvider("https://mainnet.infura.io/v3/" + project_id)) 
    checksum_addy=w3.toChecksumAddress(addy)
    if len(w3.eth.getCode(checksum_addy))>0:
        return True
    else:
        return False


def common_investors(pairlist,size):
    '''
    pairlist: list of pair addys
    size: size*1000 = amount of addys to scape for each pair
    '''
    if len(pairlist)==1:
        print("You must provide at least two pair address")
    l=intersection(get_first_investors_list(pairlist[0],size), get_first_investors_list(pairlist[1],size))
    if len(pairlist)==2:
        return l
    
    for i in pairlist[2:]:
        l=intersection(l, get_first_investors_list(i,size))
    l=list(dict.fromkeys(l))
    
    return [addy for addy in l if not is_contract(addy)]

