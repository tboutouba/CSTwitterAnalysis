import tweepy
# We import our access keys:
#from tweet_collection.credentials import *

def twitter_setup():
    """
    Utility function to setup the Twitter's API
    with an access keys provided in a file credentials.py
    :return: the authentified API
    """
    # Authentication and access using keys:
    auth = tweepy.OAuthHandler('Q3Ws9OWJElGQyNjjH97wV9few', 'Sgu7HMcCvSHTGofqu0LTIpYCmAO7JdEV9VNVBc6r8HHQDcv42c')
    auth.set_access_token('928109258-ksPsknZiwt3I0k0wAIV5envEpIlpFO0RZZPVKGmZ', 's51x413cIKtkzaBn0yoeLkaHQLCsf5V1eom2SPrN9u2mn')

    # Return API with authentication:
    api = tweepy.API(auth)
    return api
