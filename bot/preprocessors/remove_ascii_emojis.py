import re

from preprocessors import Preprocessor


class RemoveASCIIEmojis(Preprocessor):
    ascii_emoji_patterns = re.compile(
        r':\)+|:/'
    )

    @staticmethod
    def preprocess(tweet: str):
        return RemoveASCIIEmojis.ascii_emoji_patterns.sub(r'', tweet)

    @staticmethod
    def get_preprocessor_name():
        return "remove_ascii_emojis"
