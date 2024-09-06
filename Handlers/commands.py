from telegram import (
        Update,
        InlineKeyboardMarkup,
    )
from telegram.ext import (
        ContextTypes
    )

from .states import StartState
from Keyboard import InlineKeyboardBuilder


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # user_id = update.message.chat_id

    start_message = (
        'Добро пожаловать в Tome Raider⭐\n'
        'Telegram-бот для прочтения книг, которые ты сам можешь добавлять!'
        '\n'
        '\n'
        'Возможности:\n'
        '📚 Работа с книгами: поиск, добавление, чтение\n'
        '🔖 Работа с закладками: переход, создание и удаление\n'
    )

    reply_markup: InlineKeyboardMarkup = (
        InlineKeyboardBuilder()
        .add_row()
        .add_button("📚 Перейти к поиску книг",
                    callback_data=StartState.GO_TO_BOOKS)
        .add_row()
        .add_button("🔖 Перейти к закладкам",
                    callback_data=StartState.GO_TO_BOOKMARKS)
        .build()
    )

    await update.message.reply_text(
            start_message,
            reply_markup=reply_markup,
        )


async def unknown_command(update: Update,
                          context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
            'Неизвестная команда!'
        )
