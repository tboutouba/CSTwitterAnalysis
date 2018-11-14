import tweepy
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

def collect():
    connexion = twitter_setup()
    tweets = connexion.search("Emmanuel Macron",language="french",rpp=100)
    for tweet in tweets:
        print(tweet.text)

