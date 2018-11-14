import tweepy
import credentials

auth = tweepy.OAuthHandler(credentials.CONSUMER_KEY, credentials.CONSUMER_SECRET)
auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_SECRET)
api = tweepy.API(auth)

status = "Testing!"
api.update_status(status=status)
