import tweepy
import config
import csv
import pandas as pd

# API object
client = tweepy.Client(bearer_token=config.TWITTER_BEARER)

# collect 10 tweets for test
try:
    tweets = client.search_recent_tweets(query='btc', tweet_fields=['public_metrics'], max_results=10)
except:
    raise Exception('Unable to collect tweets.\n')

# Prep csv file to write to 
file = open('result.csv', 'a')
csvWriter = csv.writer(file)
csvWriter.writerow(['Tweet ID', 'Text', 'Likes'])

with file:
    for tweet in tweets.data:
        print (tweet.public_metrics['like_count'])
        csvWriter.writerow([tweet.id, tweet.text, tweet.public_metrics['like_count']])

