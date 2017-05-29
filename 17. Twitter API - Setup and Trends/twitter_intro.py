import json
import tweepy
from tweepy import OAuthHandler

CONSUMER_KEY = "eJQbPWkR77HLGXaKfWO624IYA"
CONSUMER_SECRET = "LdFFXGGU9ELy2M6xiyOI6GZqZKN9ObQgDotQtD1ZE1SNT1mfC6"
OAUTH_TOKEN = "1361549952-fpHi5hjXhWAxSIUyPhKYjNcQyRfXR1d7Sp5dmp6"
OAUTH_TOKEN_SECRET = "FZbwuF0i4YaUy3X3seAAFFkv6P6WFPvPlkpLnZsB9mGit"

auth = OAuthHandler( CONSUMER_KEY, CONSUMER_SECRET )
auth.set_access_token( OAUTH_TOKEN, OAUTH_TOKEN_SECRET )
api = tweepy.API( auth )

DUB_WOE_ID = 560743
LON_WOE_ID = 44418

dub_trends = api.trends_place( DUB_WOE_ID )
lon_trends = api.trends_place( LON_WOE_ID )

dub_trends_set = set( [trend['name']
                       for trend in dub_trends[0]['trends']] )

lon_trends_set = set( [trend['name']
                       for trend in lon_trends[0]['trends']] )

common_trends = set.intersection( dub_trends_set, lon_trends_set )

print common_trends