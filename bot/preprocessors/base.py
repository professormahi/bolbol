import os

MAX_PRIORITY = 100


class Preprocessor(object):
    DEFAULT_PREPROCESSORS = None
    PREPROCESSORS = None

    @staticmethod
    def preprocess(tweet: str):
        raise NotImplementedError

    @staticmethod
    def get_preprocessor_name():
        raise NotImplementedError

    @staticmethod
    def is_enabled_by_default():
        return True

    @staticmethod
    def priority():
        return 0

    @staticmethod
    def get_preprocessors_list() -> list:
        if Preprocessor.DEFAULT_PREPROCESSORS is None or Preprocessor.PREPROCESSORS is None:
            all_enabled_preprocessors = list(filter(
                lambda cls: cls.is_enabled_by_default(),
                Preprocessor.__subclasses__()
            ))  # list all enabled-by-default preprocessors

            # sort by priority
            all_enabled_preprocessors = sorted(all_enabled_preprocessors, key=lambda cls: cls.priority(), reverse=True)

            Preprocessor.DEFAULT_PREPROCESSORS = {cls.get_preprocessor_name(): cls for cls in all_enabled_preprocessors}

            if os.getenv("THREAD_PREPROCESSORS"):
                Preprocessor.PREPROCESSORS = [
                    Preprocessor.DEFAULT_PREPROCESSORS[p].preprocess for p in
                    os.getenv("THREAD_PREPROCESSORS").split()
                ]
            else:
                Preprocessor.PREPROCESSORS = [
                    Preprocessor.DEFAULT_PREPROCESSORS[p].preprocess for p in
                    Preprocessor.DEFAULT_PREPROCESSORS.keys()
                ]

        return Preprocessor.PREPROCESSORS

    @staticmethod
    def preprocess_thread(thread: list) -> list:
        for preprocessor in Preprocessor.get_preprocessors_list():
            thread = list(map(preprocessor, thread))
        return thread

    @staticmethod
    def process_thread_to_str(thread: list) -> str:
        thread_text = " ".join(thread)

        for preprocessor in Preprocessor.get_preprocessors_list():
            thread_text = preprocessor(thread_text)

        return thread_text
