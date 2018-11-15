# Twitter App access keys for @user

# Consume:
CONSUMER_KEY    = '1q2jMARfkgLZ13WegLqx4qr4R'
CONSUMER_SECRET = 'bhbQRK1L3eTVVyrU1wd9tybhmfKJdtSyDykw9hdE3Y0dwpRBeF'

# Access:
ACCESS_TOKEN  = '928109258-GgXa4SqhsYKCqmQooeFSCE81A8AgnkWgVKHU5rak'
ACCESS_SECRET = 'JxbAWlI2lSBVGlMfyr7zHUfdfNoCixhgKH1GPZM1YxdIY'

import tweepy

def twitter_setup():
    """
    Utility function to setup the Twitter's API
    with an access keys provided in a file credentials.py
    :return: the authentified API
    """
    # Authentication and access using keys:
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    # Return API with authentication:
    api = tweepy.API(auth)
    return(api)

def get_tweets_from_candidate_search_queries(queries,twitter_api):
    try :
        liste=[]
        for querie in queries:#pour chaque requête
            tweets = twitter_api.search(querie,language="french",rpp=100)#on va chercher les tweets correspondants
            for tweet in tweets: # on va print les tweets qu'on a trouvé
                a=tweet.text #dictionnaire et ne va selectionner que le contenu de la clé text
                liste.append(a)
        return liste
    except tweepy.TweepError: # prise en compte des erreurs
        print("Oops TweepError")
    except tweepy.RateLimiteError:
        print("Oops RateLimitError")

a=get_tweets_from_candidate_search_queries(["Emmanuel Macron","Nicolas Sarkozy"],twitter_setup())# essai avec deux requêtes
print(a)
def get_candidate_queries(num_candidate, file_path):#on va chercher les requêtes pour chaque candidat
    """
    Generate and return a list of string queries for the search Twitter API from the file file_path_num_candidate.txt
    :param num_candidate: the number of the candidate
    :param file_path: the path to the keyword and hashtag
    files
    :param type: type of the keyword, either "keywords" or "hashtags"
    :return: (list) a list of string queries that can be done to the search API independently
    """
    try:
        fichier_keywords=open(file_path+"/keywords_cadidate_n.txt",r)#récupération des requêtes dans un premier fichier
        queries1=fichier_keywords.readlines()
        fichier_keywords.close()
        fichier_hashtag=open(file_path+"/hashtag_candidate_n.txt",r)#récupération des requêtes dans un deuxième fichier
        queries2=fichier_hashtag.readlines()
        fichier_hashtag.close()
        queries=queries1+queries2
        return queries
    except IOError:
        print ("Oops IOError")

def collect(query):
   connexion = twitter_setup()
   tweets = connexion.search(query,language="french",count= 50)
   Tweets=[]
   for tweet in tweets:
       Tweets.append([tweet.created_at,tweet.id,tweet.text,tweet.in_reply_to_status_id,tweet.retweeted])
   return Tweets

tweets=collect("Emmanuel Macron")

def store_tweets(tweets,filename):
    import json
    dictionnaire={}
    for i in range (0,len(tweets)):
        dictionnaire[tweets[i][1]]=[]
        dictionnaire[tweets[i][1]].append(str(tweets[i][0]))
        dictionnaire[tweets[i][1]].append(tweets[i][2])
        dictionnaire[tweets[i][1]].append(tweets[i][3])
        dictionnaire[tweets[i][1]].append(tweets[i][4])
    print(dictionnaire)
    with open(filename+'.json', 'w', encoding='utf-8') as f:
        json.dump(dictionnaire, f)
    return dictionnaire

dictionnaire=store_tweets(tweets,'/Users/Lea/Desktop/Test')

def transform_to_dataframe(dictionnaire):
    import pandas as pd
    df = pd.DataFrame(dictionnaire)
    return df

from twitter_predictor.twitter_collect import collect
from pytest import *

def test_collect():
    tweets = tweet_collect.collect()
    data =  transform_to_dataframe(tweets)
    assert 'tweet_textual_content' in data.columns
