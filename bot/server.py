import logging
import re
from typing import Optional

from fastapi import FastAPI

from preprocessors import Preprocessor
from twitter_api import TwitterAPI

app = FastAPI()
logger = logging.getLogger('fastapi')


@app.get("/")
async def root_url():
    return {
        "stat": "OK",
        "response": "Hello World! We are the Bolbol bot and our goal is to read your Twitter threads using "
                    "a TTS service. To use our service use /read?tweet=<url to the last tweet of the thread>."
    }


@app.get("/ping")
async def ping_url():
    try:
        if TwitterAPI.get_instance().verify_credentials():
            return {
                "stat": "OK",
                "response": "pong"
            }
        else:
            return {
                "stat": "NOK",
                "response": "error"
            }
    except Exception as e:
        logger.error(f"Exception on /ping url: {e}")
        return {
            "stat": "NOK",
            "response": "error"
        }


@app.get("/read")
async def read_url(tweet: Optional[str] = None):
    groups = re.match(r"https://twitter.com/(?P<username>\w+)/status/(?P<tweet_id>\d+)$", tweet)
    if not groups:
        return {
            "stat": "NOK",
            "response": "wrong tweet format"
        }

    the_thread = TwitterAPI.get_instance().get_thread(groups["tweet_id"], only_text=True)
    the_thread_preprocessed = Preprocessor.process_thread_to_str(the_thread)

    return {
        "response": {
            "requested_tweet": tweet,
            "thread": the_thread_preprocessed
        }
    }  # TODO Send to the TTS service and publish the sound
