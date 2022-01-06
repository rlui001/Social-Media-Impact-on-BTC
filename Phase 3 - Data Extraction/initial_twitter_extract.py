import tweepy
import config
import csv

# API object
client = tweepy.Client(bearer_token=config.TWITTER_BEARER)

# collect 10 tweets for test
try:
    tweets = client.search_recent_tweets(query='btc', max_results=10)
except:
    raise Exception('Unable to collect tweets.\n')

# Prep csv file to write to 
file = open('result.csv', 'a')
csvWriter = csv.writer(file)
csvWriter.writerow(['Tweet ID', 'Text'])

with file:
    for tweet in tweets.data:
        csvWriter.writerow([tweet.id, tweet.text])