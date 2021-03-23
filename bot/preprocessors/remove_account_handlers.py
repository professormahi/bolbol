import re

from preprocessors import Preprocessor


class RemoveAccountHandlers(Preprocessor):
    account_handler_pattern = re.compile(r'@\w+\s')

    @staticmethod
    def get_preprocessor_name():
        return "remove_account_handlers"

    @staticmethod
    def preprocess(tweet: str):
        return RemoveAccountHandlers.account_handler_pattern.sub('', tweet)
