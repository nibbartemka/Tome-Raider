from typing import Protocol

from .Book import Book


class BookFormatter(Protocol):
    @staticmethod
    def generate(book: Book) -> str:
        pass


class MarkdownBookFormatter(object):
    @staticmethod
    def generate(book: Book) -> str:
        return (
            f'*Название*: {book.title}'
            '\n'
            f'*Авторы*: {", ".join(book.authors)}'
            '\n'
            f'*Жанр*: {book.genre}'
            '\n'
            '\n'
            f'*Описание*: {book.description}'
        )