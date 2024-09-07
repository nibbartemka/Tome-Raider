from telegram import (
        Update,
        InlineKeyboardMarkup,
    )
from telegram.ext import ContextTypes, ConversationHandler

from .states import ReadingState
from Books import Reader, BookReader, Book
from Keyboard import InlineKeyboardBuilder
from Bookmarks import Bookmark


async def reading(update: Update,
                  context: ContextTypes.DEFAULT_TYPE) -> None:
    if 'book' not in context.user_data:
        await update.message.reply_text(
            'Внимание: Не выбрана книга!'
        )

    book = context.user_data['book']

    if 'reader' not in context.user_data:
        context.user_data['reader'] = BookReader(book)

    reader: Reader = context.user_data['reader']
    page: str = reader.get_current_page()

    reply_markup: InlineKeyboardMarkup = (
        InlineKeyboardBuilder()
        .add_row()
        .add_button("⬅️", callback_data=ReadingState.PREVIOUS_PAGE)
        .add_button(reader.progress, callback_data=ReadingState.SELECT_PAGE)
        .add_button("➡️", callback_data=ReadingState.NEXT_PAGE)
        .add_row()
        .add_button("Добавить закладку",
                    callback_data=ReadingState.ADD_BOOKMARK)
        .add_button("Назад", callback_data=ReadingState.RETURN)
        .build()
    )

    await update.message.reply_text(
            page,
            reply_markup=reply_markup,
        )


async def update_page(update: Update,
                      context: ContextTypes.DEFAULT_TYPE) -> None:
    reader: Reader = context.user_data['reader']
    page: str = reader.get_current_page()

    reply_markup: InlineKeyboardMarkup = (
        InlineKeyboardBuilder()
        .add_row()
        .add_button("⬅️", callback_data=ReadingState.PREVIOUS_PAGE)
        .add_button(reader.progress, callback_data=ReadingState.SELECT_PAGE)
        .add_button("➡️", callback_data=ReadingState.NEXT_PAGE)
        .add_row()
        .add_button("Добавить закладку",
                    callback_data=ReadingState.ADD_BOOKMARK)
        .add_button("Назад", callback_data=ReadingState.RETURN)
        .build()
    )

    await update.message.edit_text(
        page,
        reply_markup=reply_markup
    )


async def select_page(update: Update,
                      context: ContextTypes.DEFAULT_TYPE) -> None:
    book: Book = context.user_data['book']
    await update.message.reply_text(
        f"Введите номер страницы (1-{len(book.pages)}):"
    )

    await enter_page_number(update, context)


async def enter_page_number(update: Update,
                            context: ContextTypes.DEFAULT_TYPE) -> int:
    user_input = update.message.text
    try:
        page_number: int = int(user_input)
        reader: Reader = context.user_data['reader']

        reader.move_to_page(page_number)
        await update_page(update, context)
    except ValueError:
        await update.message.reply_text(
            "Некорректные данные. Пожалуйста, введите номер страницы снова:"
        )
        await enter_page_number(update, context)


# async def add_bookmark(update: Update,
#                        context: ContextTypes.DEFAULT_TYPE) -> None:
#     # ПАКА ТАК ПАТОМ ИНАЧЕ
#     if 'bookmarks' not in context.user_data:
#         context.user_data['bookmarks'] = {}

#     bookmarks: dict[str, Bookmark] = context.user_data['bookmarks']
#     current_reader: BookReader = context.user_data['reader']

#     # bookmarks.update{
#     #     Bookmark(
#     #         current_reader.book,
#     #         current_reader.current_page_index
#     #     )
#     # }
