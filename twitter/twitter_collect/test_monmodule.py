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
    print(api)
    test="Testing 2"
    api.update_status(status=test)

twitter_setup()
