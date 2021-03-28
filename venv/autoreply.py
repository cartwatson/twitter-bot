#!/usr/bin/env python
# tweepy-bots/bots/autoreply.py

import tweepy
import logging
from config import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def check_mentions(api, keywords, since_id):
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline, since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        # if tweet.in_reply_to_status_id is not None:
        #     continue
        # if any(keyword in tweet.text.lower() for keyword in keywords):
        #     logger.info(f"Answering to {tweet.user.name}")
        #
        #     if not tweet.favorited:
        #         # Mark it as Liked, since we have not done it yet
        #         try:
        #             tweet.favorite()
        #         except Exception as e:
        #             logger.error("Error on fav", exc_info=True)
        #
        #     if not tweet.user.following:
        #         tweet.user.follow()
        #
        #     api.update_status(
        #         status= "@" + tweet.user.screen_name + " you was doing PIPI in your pampers when i was beating players much more stronger than you",
        #         in_reply_to_status_id=tweet.id,
        #     )

        #expirmental zone-----------------------------------------------------------------------------------------------
        if tweet.in_reply_to_status_id is not None:
            continue
        if "care package" in tweet.text.lower():
            logger.info(f"Answering to {tweet.user.name}")

            # Mark it as Liked
            if not tweet.favorited:
                try:
                    tweet.favorite()
                except Exception as e:
                    logger.error("Error on fav", exc_info=True)

            api.update_status(
                status= "@" + tweet.user.screen_name + " everything's going to be okay, you are loved",
                in_reply_to_status_id=tweet.id,
            )

        if "fuck robots" in tweet.text.lower():
            logger.info(f"Answering to {tweet.user.name}")

            # Mark it as Liked
            if not tweet.favorited:
                try:
                    tweet.favorite()
                except Exception as e:
                    logger.error("Error on fav", exc_info=True)

            api.update_status(
                status= "@" + tweet.user.screen_name + " its all fun and games until robots fuck you",
                in_reply_to_status_id=tweet.id,
            )
        #---------------------------------------------------------------------------------------------------------------

    return new_since_id

def main():
    api = create_api()
    since_id = 1
    while True:
        since_id = check_mentions(api, [], since_id)
        logger.info("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
    main()