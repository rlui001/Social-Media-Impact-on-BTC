# Social Media Impact on BTC
A data engineering capstone project that explores the potential impact social media has on Bitcoin.

# Current Limitations:
+ Twitter API allows monthly 2,000,000 tweet usage. Either I will need to upgrade my developer access, or make use of other historical data sets (like Kaggle) that covers 2016-2019. This means the raw data being extracted may differ in quality and expectations, as my extracts may have different criteria. Another option is to restrict the tweets that I pull from only accounts that meet a set criteria.
+ Further Twitter API limitations currently only allow me to search tweets in the past 7 days and I am unable to pull the necessary fields. An example of the data that I need is from the kaggle dataset that I will be using.
+ Pytrends API requires a wait time of 60s between requests or it will start timing out. This led to an extremely long request to pull data from 2013-2021. Fortunately, future requests will be up-to-date so it will not take long.

# To Do:
+ Update pytrends code to be more generic and pass in parameters for data request
+ Identify workarounds to twitter API limitations, or upgrade access 
+ Update kaggle code to be more generic and pass in file names for downloads
+ Create functions for all three and combine into one file
