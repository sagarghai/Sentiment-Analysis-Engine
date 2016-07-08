from tweepy import *
import simplejson as json


# class SListener(StreamListener):

#     def on_status(self, status):
#         print status

#     def on_error(self, status_code):
#         if status_code == 420:
#             return False

ACCESS_TOKEN = '745585523364814848-IHVzTunccCuHXmFlcrtEd61Xs8wPyG1'
ACCESS_SECRET = 'Jyi2LqbMluaW5k1q2yOTIb3jT28fXlU22fNkF2bBLG5UM'
CONSUMER_KEY = 'RC10RuLHntJNmjTG73h71q4T6'
CONSUMER_SECRET = 'G1uopnA6VNqpA1mx4C8qtPRFah2CKri4EIBNqUBjlFoJDT4zy8'


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
