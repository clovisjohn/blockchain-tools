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

**Restart the runtime to fix conflict errors**

> execfile ("/content/crypto-tools/early investors finder/main_PoC.py")

Add your infura project id using the variable project id

>project_id="your-project-id" (keep the quotes)

**You can now directly call the function common_investors from the python interpreter**

...More data will be added later

