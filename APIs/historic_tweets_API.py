import snscrape.modules.twitter as sntwitter
import pandas as pd
import datetime

def get_historic_tweets(start_date,end_date):
	delta = datetime.timedelta(days=1)
	list1 = []
	while start_date <= end_date:
	    list1.append((str(start_date),str(start_date+delta)))
	    start_date += delta
	for i in list1:
    maxTweets = 500

    since = 'since:'+i[0]
    until = 'until:'+i[1]
    # Creating list to append tweet data to
    

    # Using TwitterSearchScraper to scrape data and append tweets to list
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper('#BTC '+since+ ' ' + until).get_items()):
        if i>maxTweets:
            break
        tweets_list2.append([tweet.date, tweet.id, tweet.content, tweet.user.username])

    tweets_df = pd.DataFrame(tweets_list2, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

    return tweets_df