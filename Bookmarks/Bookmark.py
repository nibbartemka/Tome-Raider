from dataclasses import dataclass
from typing import Optional

from Books import Book


@dataclass(frozen=True,
           slots=True,
           init=False)
class Bookmark:
    book: Book
    page_number: int
    description: str

    def __init__(self, book: Book,
                 page_number: int,
                 description: Optional[str] = None):
        self.book = book
        self.page_number = page_number

        if description is None:
            self.description = f'{self.book.title}, с. {self.page_number}'
        else:
            self.description = f'{self.book.title} "{description}"'
