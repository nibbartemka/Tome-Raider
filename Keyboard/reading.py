from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def create_pagination_inline_keyboard(reading_progress: str,
                                      select_page_callback_data: str,
                                      previous_page_callback_data: str,
                                      next_page_callback_data: str,
                                      return_callback_date: str) -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("⬅️", callback_data=previous_page_callback_data),
            InlineKeyboardButton(reading_progress, callback_data=select_page_callback_data),
            InlineKeyboardButton("➡️", callback_data=next_page_callback_data),
        ],
        [InlineKeyboardButton("Назад", callback_data=return_callback_date)],
    ]

    return InlineKeyboardMarkup(keyboard)
