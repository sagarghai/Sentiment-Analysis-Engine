from tweepy import *
import simplejson as json

class SListener(StreamListener):

	def on_status(self, status):
		print status

	def on_error(self, status_code):
		if status_code == 420:
			return False

ACCESS_TOKEN = '3192572438-6XD1gbb1wn1QMD3ZrwNpC2l2XhJEdm3jr1PBFBZ'
ACCESS_SECRET = 'dpMEZQfmXF4jr3kFmV1S7GgVA1msSkwm6BYtRN0w5GmCW'
CONSUMER_KEY = '9SsrPbUccDScopbwdf3d9c97t'
CONSUMER_SECRET = 'b5FxmKtocLcrAzCZdHVFcan4KjXZ40Binc9yoo6QpqdITKo64d'

if __name__ == "__main__":
	S = SListener()
	oauth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	oauth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
	api=API(oauth)
	print api.search(q="worldcup")
	# myStreamListener = SListener()
	# myStream = Stream(auth = oauth, listener=myStreamListener)
	# myStream.filter(track=['python'])
# public_tweets = api.user_timeline()
# for tweet in public_tweets:
#     print tweet.text