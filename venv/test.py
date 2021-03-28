import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("e5DXi25vnrd2HWajco48Gwgs6", "OHJFumIbVKW9RFASHSxL4HwPK6NEMZFLhATwZ3wdIikZbiqmda")
auth.set_access_token("1323751470726983680-MXHU4OzmsOLe8eDHwgMWUOmpfOlpTZ", "R2wJZafhBCp20k45hvDuUmPd68lgZhwC5VaQ1fAQIXhNo")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

#follow user
# api.create_friendship("cartwatson")

#send tweet
# api.update_status("Test tweet from Tweepy Python")

#respond to mentions
tweets = api.mentions_timeline()
for tweet in tweets:
    tweet.favorite()