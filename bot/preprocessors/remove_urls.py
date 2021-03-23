import re

from preprocessors import Preprocessor, MAX_PRIORITY


class RemoveUrls(Preprocessor):
    url_pattern = re.compile(r'(https?://(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}'
                             r'|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}'
                             r'|https?://(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}'
                             r'|www\.[a-zA-Z0-9]+\.[^\s]{2,})')

    @staticmethod
    def preprocess(tweet: str):
        return RemoveUrls.url_pattern.sub('', tweet)

    @staticmethod
    def is_enabled_by_default():
        return True

    @staticmethod
    def get_preprocessor_name():
        return "remove_urls"

    @staticmethod
    def priority():
        return MAX_PRIORITY
