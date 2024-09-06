from telegram import (
        Update,
        InlineKeyboardMarkup,
    )
from telegram.ext import ContextTypes

from .states import ReadingState
from Books import Reader
from Books.ReaderFactory import ReaderFactory, ReaderType
from Keyboard import InlineKeyboardBuilder


async def reading(update: Update, context:
                  ContextTypes.DEFAULT_TYPE) -> None:
    if 'book' not in context.user_data:
        await update.message.reply_text(
            'Внимание: Не выбрана книга!'
        )

    book = context.user_data['book']

    if 'reader' not in context.user_data:
        context.user_data['reader'] = ReaderFactory.create_reader(
                ReaderType.BOOK_READER,
                book
            )

    reader: Reader = context.user_data['reader']
    page: str = reader.get_current_page()

    reply_markup: InlineKeyboardMarkup = (
        InlineKeyboardBuilder()
        .add_row()
        .add_button("⬅️", callback_data=ReadingState.PREVIOUS_PAGE)
        .add_button(reader.progress, callback_data=ReadingState.SELECT_PAGE)
        .add_button("➡️", callback_data=ReadingState.NEXT_PAGE)
        .add_row()
        .add_button("Назад", callback_data=ReadingState.RETURN)
        .build()
    )

    await update.message.reply_text(
            page,
            reply_markup=reply_markup,
        )


async def update_page(update: Update, context: 
                      ContextTypes.DEFAULT_TYPE) -> None:
    reader: Reader = context.user_data['reader']
    page: str = reader.get_current_page()

    reply_markup: InlineKeyboardMarkup = (
        InlineKeyboardBuilder()
        .add_row()
        .add_button("⬅️", callback_data=ReadingState.PREVIOUS_PAGE)
        .add_button(reader.progress, callback_data=ReadingState.SELECT_PAGE)
        .add_button("➡️", callback_data=ReadingState.NEXT_PAGE)
        .add_row()
        .add_button("Назад", callback_data=ReadingState.RETURN)
        .build()
    )

    await update.message.edit_text(
        page,
        reply_markup=reply_markup
    )


async def select_page(update: Update,
                      context: ContextTypes.DEFAULT_TYPE) -> None:
    pass
