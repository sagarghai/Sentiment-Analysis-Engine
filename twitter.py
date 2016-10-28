from tweepy import *
import simplejson as json


# class SListener(StreamListener):

#     def on_status(self, status):
#         print status

#     def on_error(self, status_code):
#         if status_code == 420:
#             return False

def takename(keywords, filename, cnt):
    # S = SListener()
    oauth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    oauth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = API(oauth)
    tweets = api.search(q=keywords, lang='en', count=cnt)
    file1 = open(filename, 'w+')
    for tweet in tweets:
        file1.write((str)(tweet))
        file1.write("\n")
