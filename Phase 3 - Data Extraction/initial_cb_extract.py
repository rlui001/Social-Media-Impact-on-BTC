import requests

pair = 'BTC-USD'
granularity = '900'
start = '2021-06-01'
end = '2021-06-02'

url = "https://api.exchange.coinbase.com/products/" + \
    pair + "/candles?granularity=" + \
    granularity + "&" + start + "&" + end


headers = {"Accept": "application/json"}

response = requests.request("GET", url, headers=headers)

print(response.text)