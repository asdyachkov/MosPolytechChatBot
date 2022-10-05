from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton


board = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
board.add(
    KeyboardButton("Главное меню", callback_data="menu"),
    KeyboardButton("Назад", callback_data="back")
    )

