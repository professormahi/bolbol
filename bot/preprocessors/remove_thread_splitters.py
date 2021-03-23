import re

from preprocessors import Preprocessor


class RemoveThreadSplitters(Preprocessor):
    thread_splitter_patterns = re.compile(
        r'\.{3}|…|\d+\\|/\d+'
    )

    @staticmethod
    def preprocess(tweet: str):
        return RemoveThreadSplitters.thread_splitter_patterns.sub('', tweet)

    @staticmethod
    def get_preprocessor_name():
        return "remove_thread_splitters"

