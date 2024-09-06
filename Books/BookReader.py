from typing import Protocol

from .Book import Book


class Reader(Protocol):
    def get_current_page(self) -> str:
        pass

    def next_page(self) -> None:
        pass

    def previous_page(self) -> None:
        pass


class BookReader(object):
    def __init__(self, book) -> None:
        self.book: Book = book
        self.current_page_index: int = 0

    @property
    def progress(self) -> str:
        return f'{self.current_page_index + 1}/{len(self.book.pages)}'

    def next_page(self) -> None:
        if self.has_next_page():
            self.current_page_index += 1

    def previous_page(self) -> None:
        if self.has_previous_page():
            self.current_page_index -= 1

    def move_to_page(self, page_index: int) -> None:
        if not (0 <= page_index <= len(self.book.pages) - 1):
            raise ValueError(
                "Incorrect page number. Please retry and enter correct value"
            )

        self.current_page_index = page_index

    def has_next_page(self) -> bool:
        return self.current_page_index + 1 < len(self.book.pages)

    def has_previous_page(self) -> bool:
        return self.current_page_index - 1 > -1

    def get_current_page(self) -> str:
        return self.book.pages[self.current_page_index]
