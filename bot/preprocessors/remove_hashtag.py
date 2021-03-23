from preprocessors import Preprocessor


class RemoveHashtag(Preprocessor):

    @staticmethod
    def preprocess(tweet: str):
        return tweet.replace("#", "")

    @staticmethod
    def get_preprocessor_name():
        return "remove_hashtag"
