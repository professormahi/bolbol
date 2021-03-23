import logging
import os

import twitter

logger = logging.getLogger('fastapi')


class TwitterAPI:
    __instance = None

    def __init__(self, **kwargs):
        if TwitterAPI.__instance is not None:
            raise Exception("This class is singleton!")
        else:
            TwitterAPI.__instance = self

            self.consumer_key = kwargs.get("consumer_key", os.getenv("TW_CONSUMER_KEY"))
            self.consumer_secret = kwargs.get("consumer_secret", os.getenv("TW_CONSUMER_SECRET"))
            self.access_token_key = kwargs.get("access_token_key", os.getenv("TW_ACCESS_TOKEN_KEY"))
            self.access_token_secret = kwargs.get("access_token_secret", os.getenv("TW_ACCESS_TOKEN_SECRET"))

            self.api = twitter.Api(
                consumer_key=self.consumer_key,
                consumer_secret=self.consumer_secret,
                access_token_key=self.access_token_key,
                access_token_secret=self.access_token_secret,
                timeout=os.getenv("TW_API_TIMEOUT", 30),
                debugHTTP=os.getenv("TW_HTTP_DEBUG", False),
                tweet_mode="extended"
            )

    @staticmethod
    def get_instance(**kwargs):
        if TwitterAPI.__instance is None:
            TwitterAPI(**kwargs)
        return TwitterAPI.__instance

    def verify_credentials(self):
        return self.api.VerifyCredentials()

    def get_thread(self, last_tweet_id, only_text=True) -> list:
        current_tweet = self.api.GetStatus(status_id=last_tweet_id).AsDict()
        thread = []

        while True:
            if only_text:
                thread.append(current_tweet["full_text"])
            else:
                thread.append({
                    "tweet_id": current_tweet["id"],
                    "tweet_id_str": current_tweet["id_str"],
                    "text": current_tweet["full_text"]
                })

            if current_tweet.get("in_reply_to_status_id", None) is None:
                break
            current_tweet = self.api.GetStatus(status_id=current_tweet["in_reply_to_status_id"]).AsDict()

        return list(reversed(thread))
