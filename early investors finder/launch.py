from functions import *


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

