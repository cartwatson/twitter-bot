# tweepy-bots/bots/config.py
import tweepy
import logging
import os

logger = logging.getLogger()

def create_api():
    consumer_key = "e5DXi25vnrd2HWajco48Gwgs6"
    consumer_secret = "OHJFumIbVKW9RFASHSxL4HwPK6NEMZFLhATwZ3wdIikZbiqmda"
    access_token = "1323751470726983680-MXHU4OzmsOLe8eDHwgMWUOmpfOlpTZ"
    access_token_secret = "R2wJZafhBCp20k45hvDuUmPd68lgZhwC5VaQ1fAQIXhNo"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api