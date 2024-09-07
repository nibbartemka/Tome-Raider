from telegram import (
        Update,
        InlineKeyboardMarkup,
    )
from telegram.ext import ContextTypes

from .states import ReadingState
from Books import Reader, BookReader
from Keyboard import InlineKeyboardBuilder
from Bookmarks import Bookmark


# def create_keyboard_by_sequence(builder, items, current_index = 0):
#     if current_index == len(items) - 1:
#         builder = (
#             builder
#             .add_row()
#             .add_button()
#         )


# async def bookmarks(update: Update,
#                     context: ContextTypes.DEFAULT_TYPE) -> None:
#     reply_markup: InlineKeyboardMarkup = (
#         InlineKeyboardBuilder()
#         .add_row()
        
#         .build()
#     )