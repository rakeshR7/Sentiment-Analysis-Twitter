import json
from twitter import Twitter, OAuth


#Configuration File
data = open("config.json")
config = json.load(data)
#print(config)
#Configuration Setup
oauth = OAuth(
    config["access_token"],
    config["access_token_secret"],
    config["consumer_key"],
    config["consumer_secret"]
          )


# Configure the OAuth using the Credentials provided
twitter = Twitter(auth=oauth)

search = twitter.GetSearch(raw_query="q=WeWantChowkidar%20&result_type=recent&since=2019-03-01&count=100")
print(search)

# fetch the Tweets and query accordingly, filtered using links
try:
    iterator = twitter.search.tweets(q='#WeWantChowkidar -filter:links ',lang='en', count=5000, since="2019-03-13", until="2019-03-18")
except:
    print("ERROR",iterator)

print(iterator['statuses'])
# list which has DICTIONARY for the Tweet JSON
tweets_q = iterator['statuses']
print(tweets_q)
# list of the users who have already tweeted, so as to fetch tweets from different user everytime
users_tweeted = []

# Tweet Count
i = 1

#For every tweet that is fetched, get only relevant tweets
for tweet in tweets_q:
        if (tweet['user']['followers_count'] > 10 and tweet['user']['screen_name'] not in users_tweeted and not tweet['text'].startswith("RT")):
            print(tweet)
            print(i,' '.join(tweet['text'].split("\n")).encode(encoding='utf-8'))
            users_tweeted.append(tweet['user']['screen_name'])
            print(users_tweeted)
            i+=1

print("tweets", tweets_q)