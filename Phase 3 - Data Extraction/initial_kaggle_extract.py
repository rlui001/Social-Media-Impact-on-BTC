import kaggle
import logging

#set logger level 
logging.basicConfig(level=logging.INFO)

#local path to save data
localdir = '/Users/ron/Desktop/Springboard/Kaggle Data/'

# ---- kaggle datasets to download ----
#bitcoin tweets dataset
btc_tweets = 'alaix14/Bitcoin-tweets-20160101-to-20190329'
#bitcoin price data
btc_price = 'mczielinski/bitcoin-historical-data'

## Code to download dataset
logging.info('Begin downloading dataset...\n')

try:
    kaggle.api.dataset_download_files(btc_price, path=localdir, unzip=True)
    logging.info('Download and unzip complete\n')

except Exception as e:
    logging.critical(f'Failed due to: {e}')

