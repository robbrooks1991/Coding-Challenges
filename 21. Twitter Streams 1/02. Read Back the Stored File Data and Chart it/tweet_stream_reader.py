import json
import pandas
import matplotlib.pyplot as plt

tweets_data_path = 'tweet_mining.json'

results = []
tweets_file = open(tweets_data_path, "r")
for tweet_line in tweets_file:
    try:
        status = json.loads(tweet_line)
        results.append(status)
    except:
        continue
print len(results)

#create a dataframe
statuses = pandas.DataFrame()

# store the text values
statuses['text'] = map(lambda status: status['text'], results)
#store the language values
statuses['lang'] = map(lambda status: status['lang'], results)
#sometimes there may not be a 'place' listed in the tweet, so set to 'None if not present
statuses['country'] = map( lambda status: status['place']['country'] if status['place'] != None else None, results )

# get each tweet language and the count of its appearence(not to be confused with programming language
tweets_by_lang = statuses['lang'].value_counts()

# create our drawing space/window (figure)
fig = plt.figure()
# add a plot area for our data on the figure - 1,1,1 means a single chart/graph
ax = fig.add_subplot( 1, 1, 1 )

# style the axes and labels of our plot
ax.tick_params( axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Tweet Languages', fontsize=15)
ax.set_ylabel('Number of tweet', fontsize=15)
ax.xaxis.label.set_color('#666666')
ax.yaxis.label.set_color('#666666')
ax.tick_params(axis='x', colors='#666666')
ax.tick_params(axis='y', colors='#666666')
#style the title
ax.set_title('Top 10 Languages', fontsize=15, color='#666666')

#plot the top 10 tweet languages and appearence count using a bar chart
tweets_by_lang[:10].plot(ax=ax, kind='bar', color='#FF7A00')

#color the spines(borders)
for spine in ax.spines.values():
    spine.set_edgecolor('#666666')

#render the graph
plt.show()