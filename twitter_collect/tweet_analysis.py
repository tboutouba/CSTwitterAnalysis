import tweepy
import numpy as np
import matplotlib.pyplot as plt
import json
import pandas as pd
from textblob import TextBlob
from textblob import Word
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
    tweets = connexion.search("realDonaldTrump",language="fr",count=100, rpp=100)
    data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['tweet_textual_content'])
    data['len']  = np.array([len(tweet.text) for tweet in tweets])
    data['ID']   = np.array([tweet.id for tweet in tweets])
    data['Date'] = np.array([tweet.created_at for tweet in tweets])
    data['Source'] = np.array([tweet.source for tweet in tweets])
    data['Likes']  = np.array([tweet.favorite_count for tweet in tweets])
    data['RTs']    = np.array([tweet.retweet_count for tweet in tweets])
    return data

#print(collect_to_pandas_dataframe())

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

def extraire_vocabulaire():
    connexion = twitter_setup()
    tweets = connexion.search("Emmanuel Macron",language="french",count=20, rpp=100)
    Tweet_conca=TextBlob('')
    for tweet in tweets:
        Tweet=TextBlob(tweet.text)
        Tweet_conca=Tweet_conca+Tweet
    for word in Tweet_conca.words:
        if Tweet_conca.words.count(word)==1 and Word(word)==Word(word).lemmatize():
            print(word)

#extraire_vocabulaire()

def prise_en_compte_de_l_opinion(data):
    pos_tweets=[]
    neg_tweets=[]
    neu_tweets=[]
    for tweet in data['tweet_textual_content']:
        if TextBlob(tweet).sentiment.polarity >0.05:
            pos_tweets.append(tweet)
        elif TextBlob(tweet).sentiment.polarity <-0.05:
            neg_tweets.append(tweet)
        else:
            neu_tweets.append(tweet)
    print("Percentage of positive tweets: {}%".format(len(pos_tweets)*100/len(data['tweet_textual_content'])))
    print("Percentage of neutral tweets: {}%".format(len(neu_tweets)*100/len(data['tweet_textual_content'])))
    print("Percentage de negative tweets: {}%".format(len(neg_tweets)*100/len(data['tweet_textual_content'])))

'''data=collect_to_pandas_dataframe()
prise_en_compte_de_l_opinion(data)'''
