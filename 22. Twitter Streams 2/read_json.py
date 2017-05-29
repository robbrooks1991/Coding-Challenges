import json
import re
import pandas
import matplotlib.pyplot as plt

tweets_data_path = 'tweet_mining.json'


def read_json(file_path):
    results = []
    tweets_file = open( file_path, "r" )
    for tweet_line in tweets_file:
        try:
            status = json.loads( tweet_line )
            results.append( status )
        except:
            continue
    return results

def is_token_in_tweet_text(token, tweet_text):
    token = token.lower()
    tweet_text = tweet_text.lower()
    match = re.search(token, tweet_text)
    if match:
        return True
    return False

results = read_json(tweets_data_path)

#create a dataframe
statuses = pandas.DataFrame()

#store the text values
statuses['text'] = map(lambda status: status['text'], results)
#store the language values
statuses['lang'] = map(lambda status: status['lang'], results)
#sometimes there may not be a 'place' listed in the tweet, so set to 'None' if not present
statuses['country'] = map(lambda status: status['place']['country'] if status['place'] != None else None, results)

# New dataframe columns
statuses['Romero'] = statuses['text'].apply(lambda status: is_token_in_tweet_text('Romero', status))
statuses['#worldbakingday'] = statuses['text'].apply(lambda status: is_token_in_tweet_text('#worldbakingday', status))
statuses['#SOUMUN'] = statuses['text'].apply(lambda status: is_token_in_tweet_text('#SOUMUN', status))
statuses['#IO17'] = statuses['text'].apply(lambda status: is_token_in_tweet_text('#IO17', status))
statuses['#LibDemManifesto'] = statuses['text'].apply(lambda status: is_token_in_tweet_text('#LibDemManifesto', status))
statuses['Bailly'] = statuses['text'].apply(lambda status: is_token_in_tweet_text('Bailly', status))
statuses['Keane'] = statuses['text'].apply(lambda status: is_token_in_tweet_text('Keane', status))
statuses['Smalling'] = statuses['text'].apply(lambda status: is_token_in_tweet_text('Smalling', status))
statuses['Gabbiadini'] = statuses['text'].apply(lambda status: is_token_in_tweet_text('Gabbiadini', status))
statuses['Dirk Kuyt'] = statuses['text'].apply(lambda status: is_token_in_tweet_text('Dirk Kuyt', status))

romero = statuses['Romero'].value_counts()[True]
worldbakingday = statuses['#worldbakingday'].value_counts()[True]
soumun = statuses['#SOUMUN'].value_counts()[True]
io17 = statuses['#IO17'].value_counts()[True]
libdemmanifesto = statuses['#LibDemManifesto'].value_counts()[True]
bailly = statuses['Bailly'].value_counts()[True]
keane = statuses['Keane'].value_counts()[True]
smalling = statuses['Smalling'].value_counts()[True]
gabbiadini = statuses['Gabbiadini'].value_counts()[True]
dirk_kuyt = statuses['Dirk Kuyt'].value_counts()[True]

print romero
print worldbakingday
print soumun
print io17
print libdemmanifesto
print bailly
print keane
print smalling
print gabbiadini
print dirk_kuyt

tweet_words = [romero, worldbakingday, soumun, io17, libdemmanifesto, bailly, keane, smalling, gabbiadini, dirk_kuyt]
tweet_names = ['Romero', 'World baking day', 'SOU vs MUN', 'IO17', 'Lib Dem Manifesto', 'Bailly', 'Keane', 'Smalling', 'Gabbiadini', 'Dirk Kuyt']
cols = ['r', 'b', 'g', 'y', 'c', 'b', 'm', 'w', 'r']

plt.pie(tweet_words,
        labels=tweet_names,
        colors=cols,
        startangle=90,
        shadow=False,
        explode=(0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
        autopct='%1.1f%%' )

plt.title('Tweets of the day')
plt.show()
