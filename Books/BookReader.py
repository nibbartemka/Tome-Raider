from typing import Protocol

from .Book import Book


class Reader(Protocol):
    def get_current_page(self) -> str:
        pass

    def next_page(self) -> None:
        pass

    def previous_page(self) -> None:
        pass

    def move_to_page(self, page_number: int) -> None:
        pass


class BookReader(object):
    def __init__(self, book) -> None:
        self.__book: Book = book
        self.__current_page_index: int = 0

    @property
    def progress(self) -> str:
        return f'{self.__current_page_index + 1}/{len(self.__book.pages)}'

    @property
    def book(self) -> Book:
        return self.__book

    @property
    def current_page_index(self) -> int:
        return self.__current_page_index

    def next_page(self) -> None:
        if self.has_next_page():
            self.__current_page_index += 1

    def previous_page(self) -> None:
        if self.has_previous_page():
            self.__current_page_index -= 1

    def move_to_page(self, page_number: int) -> None:
        page_index: int = page_number - 1

        if not (0 <= page_index <= len(self.__book.pages) - 1):
            raise ValueError(
                "Incorrect page number. Please retry and enter correct value"
            )

        self.__current_page_index = page_index

    def has_next_page(self) -> bool:
        return self.__current_page_index + 1 < len(self.__book.pages)

    def has_previous_page(self) -> bool:
        return self.__current_page_index - 1 > -1

    def get_current_page(self) -> str:
        return self.__book.pages[self.__current_page_index]
