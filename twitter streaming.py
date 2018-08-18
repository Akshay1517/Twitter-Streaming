try:
    import json
except ImportError:
    import simplejson as json


from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
ACCESS_TOKEN = '**************************************************'
ACCESS_SECRET = '*****************************************'
CONSUMER_KEY = '*********************'
CONSUMER_SECRET = '**************************************************'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter_userstream = TwitterStream(auth=oauth, domain='userstream.twitter.com')
iterator = twitter_userstream.statuses.filter(track="Google", language="en")
tweet_count = 1
for tweet in iterator:
    tweet_count -= 1
    print (json.dumps(tweet)  )
    print("\t")   
    if tweet_count <= 0:
        break 