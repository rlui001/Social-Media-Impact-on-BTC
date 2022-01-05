import pandas as pd
import time
import logging
from pytrends.request import TrendReq

# set up logger
logging.basicConfig(level=logging.INFO)

# Connect to Google
pytrend = TrendReq(hl='en-US', tz=0, retries=10)

# keywords to use
keywords = ['bitcoin', 'btc']

dataset = []
# attempt payload
try:
    logging.info(f'Attempting payload with keywords...\n')

    #pytrend.build_payload(keywords,timeframe='2013-01-01 2021-12-31')

    data = pytrend.get_historical_interest(keywords, year_start=2013, year_end=2021, month_end=12, sleep=60)
    
    if not data.empty:
        dataset.append(data)
        result = pd.concat(dataset, axis=1)
        result.to_csv('google_trends.csv')

    logging.info('Completed!')
    

except Exception as e:
    logging.critical(f'Failed payload due to {e}')