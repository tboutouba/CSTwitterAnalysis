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
    for querie in queries:
        tweets = twitter_api.search(querie,language="french",rpp=100)
        for tweet in tweets:
            print(tweet.text) #dictionnaire et ne va selectionner que le contenu de la clé text
    #except TweepError :
        #print("Oops TweepError")
    #except RateLimiteError :
        #print("Oops RateLimitError")


get_tweets_from_candidate_search_queries(["Emmanuel Macron","Nicolas Sarkozy"],twitter_setup())

def get_candidate_queries(num_candidate, file_path):
    """
    Generate and return a list of string queries for the search Twitter API from the file file_path_num_candidate.txt
    :param num_candidate: the number of the candidate
    :param file_path: the path to the keyword and hashtag
    files
    :param type: type of the keyword, either "keywords" or "hashtags"
    :return: (list) a list of string queries that can be done to the search API independently
    """
    #try:
        fichier_keywords=open(file_path+"/keywords_cadidate_n.txt",r)
        queries1=fichier_keywords.readlines()
        fichier_keywords.close()
        fichier_hashtag=open(file_path+"/hashtag_candidate_n.txt",r)
        queries2=fichier_hashtag.readlines()
        fichier_hashtag.close()
        queries=queries1+queries2
    except IOError:
        print ("Oops IOError")
