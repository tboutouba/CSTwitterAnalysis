import tweepy
from tweepy.streaming import StreamListener
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

'''def GetRetweets(statusid, count=None, trim_user=False):
    api=twitter_setup()
    """Returns up to 100 of the first retweets of the tweet identified by statusid    
    Args:
          statusid (int):
            The ID of the tweet for which retweets should be searched for
          count (int, optional):
            The number of status messages to retrieve.
          trim_user (bool, optional):
            If True the returned payload will only contain the user IDs,
            otherwise the payload will contain the full user data item.
    Returns:
          A list of twitter.Status instances, which are retweets of statusid
        """
    url = '%s/statuses/retweets/%s.json' % (api.base_url, statusid)
    parameters = {'trim_user': enf_type('trim_user', bool, trim_user),}

    if count:
         parameters['count'] = enf_type('count', int, count)

    resp = api._RequestUrl(url, 'GET', data=parameters)
    data = api._ParseAndCheckTwitter(resp.content.decode('utf-8'))

    return [Status.NewFromJsonDict(s) for s in data]
GetRetweets(1062702105788596224)'''

def collect_by_user(user_id):
    #On stocke les tweets de user_id dans une liste de couples (tweet_id, tweet_text)
    connexion = twitter_setup()
    statuses = connexion.user_timeline(id = user_id, count = 200)
    Tweets=[]
    for status in statuses:
        Tweets.append((status.id,status.text))
    print(Tweets)

'''Pour tester on peut appeler le programme
collect_by_user('realDonaldTrump')'''

#Ce programme n'est pas necessaire a la suite, mais me permet de mieux comprendre les commandes api
def collect_retweets_of_latest_tweet(user_id):
    #On stocke les tweets de user_id dans une liste de couples (tweet_id, tweet_text)
    connexion = twitter_setup()
    statuses = connexion.user_timeline(id = user_id, count = 1)
    Tweets=[]
    for status in statuses:
        Tweets.append((status.id,status.text))
    Retweets=connexion.search(Tweets[0][0],rpp=100)
    List_of_retweets=[]
    for element in Retweets:
        List_of_retweets.append(element.text)
    print (set(List_of_retweets))

'''Pour tester on peut appeler le programme
collect_retweets_of_latest_tweet('realDonaldTrump')'''

def collect_retweets_of_tweet(tweet_id):
    connexion=twitter_setup()
    Retweets=connexion.search(tweet_id,rpp=100, count = 1)
    List_of_retweets=[]
    for element in Retweets:
        List_of_retweets.append(element)
    print(List_of_retweets)



