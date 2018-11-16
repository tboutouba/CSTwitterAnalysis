import tweepy
import numpy as np
import matplotlib.pyplot as plt
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

def collect_to_pandas_dataframe():
    connexion = twitter_setup()
    tweets = connexion.search("@EmmanuelMacron",language="fr",count=50, rpp=100)
    data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweet_textual_content'])
    data['len']  = np.array([len(tweet.text) for tweet in tweets])
    data['ID']   = np.array([tweet.id for tweet in tweets])
    data['Date'] = np.array([tweet.created_at for tweet in tweets])
    data['Source'] = np.array([tweet.source for tweet in tweets])
    data['Likes']  = np.array([tweet.favorite_count for tweet in tweets])
    data['RTs']    = np.array([tweet.retweet_count for tweet in tweets])
    return data

#collect_to_pandas_dataframe()

def RTs():
    rt_max  = np.max(data['RTs'])
    rt  = data[data.RTs == rt_max].index[0]
    # Max RTs:
    print("The tweet with more retweets is: \n{}".format(data['tweet_textual_content'][rt]))
    print("Number of retweets: {}".format(rt_max))
    print("{} characters.\n".format(data['len'][rt]))

'''data=collect_to_pandas_dataframe()
RTs()'''

def Like(): #return the tweet with the highest likes
    like_max=np.max(data['Likes'])
    lk  = data[data.Likes == like_max].index[0]
    # Max Likes:
    print("The tweet with more likes is: \n{}".format(data['tweet_textual_content'][lk]))
    print("Number of likes: {}".format(like_max))
    print("{} characters.\n".format(data['len'][lk]))

'''data=collect_to_pandas_dataframe()
print(data)
Like()'''

def Likes_vs_RTs(data):
    tfav = pd.Series(data=data['Likes'].values, index=data['Date'])
    tret = pd.Series(data=data['RTs'].values, index=data['Date'])

    # Likes vs retweets visualization:
    tfav.plot(figsize=(16,4), label="Likes", legend=True)
    tret.plot(figsize=(16,4), label="Retweets", legend=True)

    plt.show()

'''data=collect_to_pandas_dataframe()
Likes_vs_RTs(data)'''
