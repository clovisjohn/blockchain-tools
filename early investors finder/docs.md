# Breakdown:

*Given a list of tokens and token pairs, return a list of addresses which were the first to buy the token*


## Requirement
* Python 3+
* web3 python library
* infura project id


## Installation
```
!git clone https://github.com/clovisjohn/crypto-tools.git
```

## Usage
You can run this script by using `launch.py size:size dex1:addy1 dex2:addy2 dex:pair`

### Arguments
- size:size : The amount of addresses to scrape for each token. This will be multiplied by 1000. For example, if you give size:10 as argument the script will return the addresses that were in the 15000 first to invest in the specified tokens.


- dex1:addy1 : It's the address of the token/pair and the dex where it can be found. Available dexes are uniswap-v3, uniswap-v2, sushiswap(ethereum). You can provide as many token/pair as you want
  
  For uniswap-v2 and sushiswap, you must provide the pair contract address(OHM-ETH, ENS-DAI,etc)\
  For uniswap-v3 you must provide the token contract address (OHM, ENS, etc)
  
  Example(ENS and OHM-DAI): uniswap-v3:0xc18360217d8f7ab5e7c516566761ea12ce7f9d72 sushiswap:0x34d7d7aaf50ad4944b70b320acb24c95fa2def7c
               
### Example
The following line will retrieve addresses that were in the 15000 first to invest in ENS and OHM-DAI 
```
launch.py size:15 uniswap-v3:0xc18360217d8f7ab5e7c516566761ea12ce7f9d72 sushiswap:0x34d7d7aaf50ad4944b70b320acb24c95fa2def7c
```

**The chat history file can be exported from the telegram desktop app, select export as html**

## Colab workflow
```
!git clone https://github.com/clovisjohn/crypto-tools.git
!pip install web3
!python /content/crypto-tools/early\ investors\ finder/launch.py size:size dex1:addy1 dex2:addy2 dex:pair
