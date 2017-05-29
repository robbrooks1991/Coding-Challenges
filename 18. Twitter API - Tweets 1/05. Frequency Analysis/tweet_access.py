import json
import tweepy
from tweepy import OAuthHandler
from collections import Counter

CONSUMER_KEY = "eJQbPWkR77HLGXaKfWO624IYA"
CONSUMER_SECRET = "LdFFXGGU9ELy2M6xiyOI6GZqZKN9ObQgDotQtD1ZE1SNT1mfC6"
OAUTH_TOKEN = "1361549952-fpHi5hjXhWAxSIUyPhKYjNcQyRfXR1d7Sp5dmp6"
OAUTH_TOKEN_SECRET = "FZbwuF0i4YaUy3X3seAAFFkv6P6WFPvPlkpLnZsB9mGit"

auth = OAuthHandler( CONSUMER_KEY, CONSUMER_SECRET )
auth.set_access_token( OAUTH_TOKEN, OAUTH_TOKEN_SECRET )
api = tweepy.API( auth )

count = 50
query = 'Weather'

# Get all tweet for the seach query
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

status_texts = [ status._json['text'] for status in results ]

screen_names = [ status._json['user']['screen_name']
                for status in results
                for mention in status._json['entities']['user_mentions'] ]

hashtags = [ hashtag['text']
            for status in results
            for hashtag in status._json['entities']['hashtags'] ]

words = [ w for t in status_texts
          for w in t.split() ]

for entry in [screen_names, hashtags, words]:
    counter = Counter(entry)
    print counter.most_common()[:10] # the top 10 results
    print