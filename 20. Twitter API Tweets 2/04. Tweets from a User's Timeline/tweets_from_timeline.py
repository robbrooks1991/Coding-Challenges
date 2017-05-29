import tweepy
from tweepy import OAuthHandler

CONSUMER_KEY = "eJQbPWkR77HLGXaKfWO624IYA"
CONSUMER_SECRET = "LdFFXGGU9ELy2M6xiyOI6GZqZKN9ObQgDotQtD1ZE1SNT1mfC6"
OAUTH_TOKEN = "1361549952-fpHi5hjXhWAxSIUyPhKYjNcQyRfXR1d7Sp5dmp6"
OAUTH_TOKEN_SECRET = "FZbwuF0i4YaUy3X3seAAFFkv6P6WFPvPlkpLnZsB9mGit"

auth = OAuthHandler( CONSUMER_KEY, CONSUMER_SECRET )
auth.set_access_token( OAUTH_TOKEN, OAUTH_TOKEN_SECRET )

api = tweepy.API( auth )

user = api.get_user('@brooksr144')

print user.screen_name
print user.followers_count

for status in tweepy.Cursor( api.home_timeline ).items( 10 ):
    # Process a tweet
    print status.text