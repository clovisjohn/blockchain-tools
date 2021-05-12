# Quick doc

## common_investors(pairlist,size)
* pairlist: list of uniswap token pairs

**Example:** 
> ["0x811beed0119b4afce20d2583eb608c6f7af1954f","0xf82d8ec196fb0d56c6b82a8b1870f09502a49f88"]
* size: size*1000 is the ammount of addresses (starting from the first to buy the token) to scrape for each pair

**Full example**
> common_investors(["0x811beed0119b4afce20d2583eb608c6f7af1954f","0xf82d8ec196fb0d56c6b82a8b1870f09502a49f88"],15)


# Colab workflow

> !pip install web3

> !git clone https://github.com/clovisjohn/crypto-tools.git

> !python /content/crypto-tools/early\ investors\ finder/main_PoC.py

> execfile ("/content/crypto-tools/early investors finder/main_PoC.py")

> common_investors(pairlst, size) #You can now directly call the funcion

In case of conflict error, restart the runtime

...More data will be added later

