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
def collect_answers_of_latest_tweet(user_id):
    #On stocke les tweets de user_id dans une liste de couples (tweet_id, tweet_text)
    connexion = twitter_setup()
    statuses = connexion.user_timeline(id = user_id, count = 1)
    Tweets=[]
    for status in statuses:
        Tweets.append((status.id,status.text))
    Answers=connexion.search(Tweets[0][0],rpp=100)
    List_of_answers=[]
    for element in Answers:
        List_of_answers.append(element.text)
    print (set(List_of_aswers))

'''Pour tester on peut appeler le programme
collect_answers_of_latest_tweet('realDonaldTrump')'''

def get_replies_to_candidate(id_candidate):
    connexion = twitter_setup()
    statuses = connexion.user_timeline(id = id_candidate, count = 10)
    Tweets=[]
    for status in statuses:
        Tweets.append((status.id,status.text))
    Answers=[]
    for i in range(len(Tweets)):
        Answers_of_tweet=connexion.search(Tweets[i][0],rpp=20)
        for element in Answers_of_tweet:
            if element.in_reply_to_status_id == Tweets[i][0]:
                Answers.append([Tweets[i][0],element.id, element.text])
    print(Answers)


'''def collect_retweets_of_tweet(tweet_id):
    connexion=twitter_setup()
    Retweets=connexion.search(tweet_id,rpp=100, count = 1)
    List_of_retweets=[]
    for element in Retweets:
        List_of_retweets.append(element)
    print(List_of_retweets)'''

def get_retweet_of_candidate(num_candidate,amount_evaluated):
   connexion = twitter_setup()
   statuses = connexion.user_timeline(num_candidate, count=10)
   for status in statuses:
       retweets = connexion.retweets(status.id,amount_evaluated)
       for tweet in retweets:
           print(tweet.text)
'''get_retweet_of_candidate(25073877,10)'''


