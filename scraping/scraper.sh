keywords=(earthquake fire hurricane tornado flood tsunami avalanche typhoon cyclone)
snscrape --max-results 100 twitter-search "disaster since:2015-12-31 until:2020-10-25" > disaster_tweets.txt
for keyword in ${keywords[*]}
do
  snscrape --max-results 100 twitter-search "$keyword since:2015-12-31 until:2020-10-25" >> disaster_tweets.txt
done
