from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Вопросы ЦПД
boards = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
boards.add(
    KeyboardButton("Главное меню", callback_data="b_b6"),
    KeyboardButton("Назад", callback_data="b_b7")
)
