from abc import ABC, abstractmethod
from typing import TypeAlias

from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup

Keyboard: TypeAlias = ReplyKeyboardMarkup | InlineKeyboardMarkup


class KeyboardBuilder(ABC):
    @abstractmethod
    def add_button(self, text: str,
                   callback_data: str, **kwargs) -> 'KeyboardBuilder':
        pass

    @abstractmethod
    def add_row(self) -> 'KeyboardBuilder':
        pass

    @abstractmethod
    def build(self) -> Keyboard:
        pass