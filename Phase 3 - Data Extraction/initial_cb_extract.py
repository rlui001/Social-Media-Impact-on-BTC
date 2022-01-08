import requests
import csv
import pandas as pd
# TO-DO: Convert into a function that takes parameters to replace below
# TO-DO: Set up iterator to do several requests 
pair = 'BTC-USD'
granularity = '300'
start = '2021-06-01'
end = '2021-06-022'

url = "https://api.exchange.coinbase.com/products/" + \
    pair + "/candles?granularity=" + \
    granularity + "&start=" + start + "&end=" + end

response = requests.get(url).json()

df = pd.DataFrame(response, columns=['time', 'low', 'high', 'open', 'close', 'volume'])

if df.empty:
    print ('Failed to retrieve Coinbase data.\n')
else:
    print (df.head())
    df.to_csv('results_cb.csv')