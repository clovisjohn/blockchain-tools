# Quick doc

## common_investors(pairlist,size)
* pairlist: list of uniswap token pairs with dexes names

  pairlist=[(address,dex_name), (address,dex_name)]
  
  ```
  Available dexes are: uniswap-v2, uniswap-v3, sushiswap
  For the address, you must use the pair contract address if you use uniswap-v2 or sushiswap (OHM-DAI pool contract address for example)
  If you use uniswap-v3, you must specify the token contract address(OHM contract address for example)
  ```

  **Example:** 
  ```
  lobi=('0xdec41db0c33f3f6f3cb615449c311ba22d418a8d','uniswap-v3')
  cvxeth=('0x05767d9ef41dc40689678ffca0608878fb3de906','sushiswap')
  pairlist=[lobi,cvxeth]
  ```
* size: size*1000 is the amount of addresses (starting from the first one to buy the token) to scrape for each pair

**Full example**
> common_investors([('0xdec41db0c33f3f6f3cb615449c311ba22d418a8d','uniswap-v3'),('0x05767d9ef41dc40689678ffca0608878fb3de906','sushiswap')],15)


# Colab workflow

> !pip install web3

> !git clone https://github.com/clovisjohn/crypto-tools.git

**Restart the runtime to fix conflict errors**

> execfile ("/content/crypto-tools/early investors finder/main_PoC.py")

Add your infura project id using the variable project id

>project_id="your-project-id" (keep the quotes)

**You can now directly call the function common_investors from the python interpreter**

...More data will be added later

