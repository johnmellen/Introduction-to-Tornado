# tweet_rate_oauth_py33.py

from oauthlib import oauth1     # oauthlib supports Python 3.3.

# The following four credentials are issued by Twitter after
# an application has been registered.
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

def oauth(url):
	client = oauth1.Client(
		CONSUMER_KEY,
		client_secret=CONSUMER_SECRET,
		resource_owner_key=ACCESS_TOKEN,
		resource_owner_secret=ACCESS_TOKEN_SECRET
		)

	header = client.sign(url)   # client.sign(url) returns a tuple of 3 elements. The
	return header[1]            # oneth element holds the authorization keys, nonce, etc.
