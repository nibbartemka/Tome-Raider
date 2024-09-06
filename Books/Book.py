from dataclasses import dataclass
from typing import Sequence


@dataclass(frozen=True, slots=True)
class Book:
    title: str
    description: str
    genre: str
    authors: Sequence[str]
    pages: Sequence[str]
