import tweepy
import json
import pandas as pd
# We import our access keys:
import credentials


def twitter_setup():
    """
    Utility function to setup the Twitter's API
    with an access keys provided in a file credentials.py
    :return: the authentified API
    """
    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
    auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_SECRET)

    # Return API with authentication:
    api = tweepy.API(auth)
    return api

def collect(query):
    connexion = twitter_setup()
    tweets = connexion.search(query,language="french",count= 50)
    Tweets=[]
    for tweet in tweets:
        Tweets.append((tweet.created_at,tweet.id,tweet.text,tweet.in_reply_to_status_id,tweet.retweeted))
    return Tweets

def store_tweets(tweets,filename):
   dictionnaire={}
   for i in range (0,len(tweets)):
       dictionnaire[tweets[i][1]]=[]
       dictionnaire[tweets[i][1]].append(str(tweets[i][0]))
       dictionnaire[tweets[i][1]].append(tweets[i][2])
       dictionnaire[tweets[i][1]].append(tweets[i][3])
       dictionnaire[tweets[i][1]].append(tweets[i][4])
   return dictionnaire
   with open(filename+'.json', 'w', encoding='utf-8') as f:
       json.dump(dictionnaire, f)

store_tweets(collect('realDonaldTrump'),'/Users/mac/Desktop/centrale/twitterPredictor/stockage')

df = pd.DataFrame(store_tweets(collect('realDonaldTrump'),'/Users/mac/Desktop/centrale/twitterPredictor/stockage'))
print(df)
