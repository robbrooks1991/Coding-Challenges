from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

CONSUMER_KEY = "eJQbPWkR77HLGXaKfWO624IYA"
CONSUMER_SECRET = "LdFFXGGU9ELy2M6xiyOI6GZqZKN9ObQgDotQtD1ZE1SNT1mfC6"
OAUTH_TOKEN = "1361549952-fpHi5hjXhWAxSIUyPhKYjNcQyRfXR1d7Sp5dmp6"
OAUTH_TOKEN_SECRET = "FZbwuF0i4YaUy3X3seAAFFkv6P6WFPvPlkpLnZsB9mGit"

keyword_list = ['#ARSSUN', 'Emirates', '#BondTrumpBond', 'Pickford', 'Defoe', 'Giroud', 'Holding'] #track list

class MyStreamListener(StreamListener):

    def on_data(self, data):
        try:
            with open('tweet_mining.json', 'a') as tweet_file:
                tweet_file.write(data)
                return True
        except BaseException as e:
            print "Failed on_data: %s" % str(e)
        return True

    def on_error(self, status):
        print status
        return True

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

twitter_stream = Stream(auth, MyStreamListener())
twitter_stream.filter(track=keyword_list)
