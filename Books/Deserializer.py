from typing import Protocol

from .Book import Book


class BookDeserializer(Protocol):
    @staticmethod
    def deserialize_book(raw_data: str) -> Book:
        pass


class JSONDeserializer(object):
    @staticmethod
    def deserialize_book(raw_data: str) -> Book:
        import json

        return Book(
                **(json.loads(raw_data))
            )
