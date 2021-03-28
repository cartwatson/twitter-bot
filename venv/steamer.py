import json
import tweepy

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(f"{tweet.user.name}:{tweet.text}")

    def on_error(self, status):
        print("Error detected")

# Authenticate to Twitter
auth = tweepy.OAuthHandler("e5DXi25vnrd2HWajco48Gwgs6", "OHJFumIbVKW9RFASHSxL4HwPK6NEMZFLhATwZ3wdIikZbiqmda")
auth.set_access_token("1323751470726983680-MXHU4OzmsOLe8eDHwgMWUOmpfOlpTZ", "R2wJZafhBCp20k45hvDuUmPd68lgZhwC5VaQ1fAQIXhNo")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

# make stream
# tweets_listener = MyStreamListener(api)
# stream = tweepy.Stream(api.auth, tweets_listener)
# stream.filter(track=["summon droid cartwatson"], languages=["en"])

# respond to mentions
tweets = api.mentions_timeline()
for tweet in tweets:
    # tweet.favorite()
    tweetid = api.mentions_timeline
    print("tweetid: ", end='')
    print(tweetid)
    api.update_status("present", in_reply_to_status_id = tweetid)

