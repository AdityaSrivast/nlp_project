import pandas as pd
import time
import tweepy
from tweepy.auth import OAuthHandler


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

tweet_url = pd.read_csv("disaster_tweets.txt",
                        index_col=None, header=None, names=["links"])


def getId(x): return x["links"].split("/")[-1]

tweet_url['id'] = tweet_url.apply(getId, axis=1)

ids = tweet_url['id'].tolist()
# print(ids)

# fetch tweets on the basis of their IDs
def fetch_tw(ids, keyword):
  list_of_tw_status = api.statuses_lookup(ids, tweet_mode="extended")
  empty_data = pd.DataFrame()
  for status in list_of_tw_status:
    tweet_elem = {"keyword": keyword,
                  "location": status.user.location,
                  "text": status.full_text,
                  "type": 0}
    empty_data = empty_data.append(tweet_elem, ignore_index=True)
  empty_data.to_csv("data_train.csv", mode="a")

keywords=['disaster','earthquake', 'fire', 'hurricane', 'tornado', 'flood', 'tsunami', 'avalanche', 'typhoon', 'cyclone']
chunks = 10 # as we are scraping 10 keywords

for i in range(chunks):
  batch = ids[i*100:(i+1)*100]
  result = fetch_tw(batch,keywords[i])

