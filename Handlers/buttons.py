from telegram import (
        Update,
        CallbackQuery
    )
from telegram.ext import ContextTypes

from .states import ReadingState, DetailState, StartState
from .reading import reading, select_page, update_page
from .detail import detail
from .commands import start


async def detail_button(update: Update, context:
                        ContextTypes.DEFAULT_TYPE) -> None:
    query: CallbackQuery = update.callback_query

    await query.answer()

    match query.data:
        case DetailState.START_READ.value:
            await reading(query, context)
        case DetailState.RATE.value:
            # Добавить функционал
            pass
        case DetailState.RETURN.value:
            # Пока на главный экран возвращаем, потом на поиск
            await start(query, context)
        case _:
            pass


async def reading_button(update: Update,
                         context: ContextTypes.DEFAULT_TYPE) -> None:
    query: CallbackQuery = update.callback_query

    await query.answer()

    match query.data:
        case ReadingState.SELECT_PAGE.value:
            await select_page(query, context)
        case ReadingState.PREVIOUS_PAGE.value:
            reader = context.user_data['reader']
            reader.previous_page()
            await update_page(query, context)
        case ReadingState.NEXT_PAGE.value:
            reader = context.user_data['reader']
            reader.next_page()
            await update_page(query, context)
        case ReadingState.RETURN.value:
            await detail(query, context)
        case _:
            pass


async def start_button(update: Update,
                       context: ContextTypes.DEFAULT_TYPE) -> None:
    query: CallbackQuery = update.callback_query

    await query.answer()

    match query.data:
        case StartState.GO_TO_BOOKS.value:
            # Заменить
            await detail(query, context)
        case StartState.GO_TO_BOOKMARKS.value:
            # Добавить
            pass
        case _:
            pass
