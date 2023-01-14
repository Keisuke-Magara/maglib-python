from typing import Literal


class Normalizer:

    @property
    def encoding(self):
        return self.__encoding

    @encoding.getter
    def encoding(self):
        return self.__encoding

    def __init__(self, encoding: Literal['ascii'] | Literal['unicode'] = 'unicode') -> None:
        self.__encoding = encoding
        if encoding == 'unicode':
            import unicodedata
        pass

    def normalize(self, string: str) -> str:
        retval = string
        return retval
