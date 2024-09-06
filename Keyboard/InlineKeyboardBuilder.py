from typing import TypeAlias, Sequence
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from .KeyboardBuilder import KeyboardBuilder

KeyboardItems: TypeAlias = Sequence[Sequence[InlineKeyboardButton] | None]


class InlineKeyboardBuilder(KeyboardBuilder):
    def __init__(self) -> None:
        self.keyboard: KeyboardItems = []

    def add_button(self, text: str,
                   callback_data: str, **kwargs) -> 'InlineKeyboardBuilder':
        self.keyboard[-1].append(
            InlineKeyboardButton(
                text=text,
                callback_data=callback_data,
                **kwargs
            )
        )
        return self

    def add_row(self) -> 'InlineKeyboardBuilder':
        self.keyboard.append([])
        return self

    def build(self) -> InlineKeyboardMarkup:
        return InlineKeyboardMarkup(self.keyboard)
