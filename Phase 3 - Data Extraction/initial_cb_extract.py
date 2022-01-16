import requests
import csv
import pandas as pd
from datetime import datetime
from datetime import timedelta

def coinbase_historical_data(start, end, pair='BTC-USD', granularity='300'):
    """
    Pulls historical candlestick data from coinbase based on parameters.
    start: start date to pull historical data, format YYYY-MM-DD
    end: end date to pull historical data, format YYYY-MM-DD
    pair: coinbase pairing, eg. BTC-USD or ETH-USD
    granularity: time interval between price points. 60=1m, 300=5m, 900=15m...
    """
    # delta sets to daily increment
    delta = timedelta(days=1)

    # local start date gets incremented, end_date is static
    local_start_date = datetime.strptime(start, '%Y-%m-%d')
    end_date = datetime.strptime(end, '%Y-%m-%d')

    # while local date has not passed the end date, keep grabbing data
    while local_start_date <= end_date:
        # URL to send GET request
        local_start_str = datetime.strftime(local_start_date, '%Y-%m-%d')
        local_end_str = datetime.strftime(local_start_date + delta, '%Y-%m-%d')

        url = "https://api.exchange.coinbase.com/products/" + \
        pair + "/candles?granularity=" + \
        granularity + "&start=" + local_start_str + "&end=" + local_end_str

        response = requests.get(url).json()

        df = pd.DataFrame(response, columns=['time', 'low', 'high', 'open', 'close', 'volume'])

        if df.empty:
            raise ValueError('Failed to retrieve Coinbase data.\n')
        else:
            print (df.head(1))
            df.to_csv('results_cb.csv', mode='a', index=False, header=False)

            # update local dates for next iteration
            local_start_date += delta
    

coinbase_historical_data('2021-03-31', '2021-12-31')