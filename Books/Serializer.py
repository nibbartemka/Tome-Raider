from typing import Protocol

from .Book import Book


class BookSerializer(Protocol):
    @staticmethod
    def serialize_book(book: Book) -> str:
        pass


class JSONSerializer(object):
    @staticmethod
    def serialize_book(book: Book) -> str:
        import dataclasses
        import json

        return json.dumps(
                dataclasses.asdict(book)
            )
