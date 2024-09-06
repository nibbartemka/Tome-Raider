import enum

from .BookReader import Reader, BookReader
from .Book import Book


@enum.unique
class ReaderType(enum.IntEnum):
    BOOK_READER = 0


class ReaderFactory(object):
    @staticmethod
    def create_reader(reader_type: ReaderType, book: Book) -> Reader:
        match reader_type:
            case ReaderType.BOOK_READER:
                return BookReader(book)
            case _:
                raise ValueError("Entered reader type doesn't exist")