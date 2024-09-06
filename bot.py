import os

from dotenv import load_dotenv
from telegram.ext import (
        Application,
        CommandHandler,
        MessageHandler,
        CallbackQueryHandler,
        filters,
    )

from Database import database_init
from Handlers.buttons import reading_button, detail_button, start_button
from Handlers.commands import start, unknown_command

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')


def main():
    database_init()

    app = (
        Application.builder()
        .token(BOT_TOKEN)
        .build()
    )

    start_handler = CommandHandler('start', start)
    start_buttons_handler = CallbackQueryHandler(
            start_button,
            '^start_'
        )
    detail_buttons_handler = CallbackQueryHandler(
            detail_button,
            '^detail_'
        )
    reading_buttons_handler = CallbackQueryHandler(
            reading_button,
            '^reading_'
        )
    unknown_command_handler = MessageHandler(filters.COMMAND,
                                             unknown_command)

    app.add_handlers([
        start_handler,
        start_buttons_handler,
        detail_buttons_handler,
        reading_buttons_handler,
        unknown_command_handler
    ])

    app.run_polling()


if __name__ == '__main__':
    main()
