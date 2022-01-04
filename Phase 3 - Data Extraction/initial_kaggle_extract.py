import kaggle
import logging

#set logger level 
logging.basicConfig(level=logging.INFO)

#test api connection
api = kaggle.api
print (api.get_config_value('username'))

## Code to download dataset
logging.info('Begin downloading dataset...\n')

try:
    kaggle.api.dataset_download_files('alaix14/Bitcoin-tweets-20160101-to-20190329', \
        path='/Users/ron/Desktop/Springboard/Kaggle Data/',\
             unzip=True)
    logging.info('Download and unzip complete\n')

except Exception as e:
    logging.critical(f'{e}')
