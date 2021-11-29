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
