from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


button1 = InlineKeyboardButton("Технологическое предпринимательство", callback_data="btn1")
inline_btn1 = InlineKeyboardMarkup().add(button1)

button2 = InlineKeyboardButton("Ликвидация расхождений в учебных планах", callback_data="btn2")
inline_btn2 = InlineKeyboardMarkup().add(button2)

button3 = InlineKeyboardButton("Перезачет дисциплины", callback_data="btn3")
inline_btn3 = InlineKeyboardMarkup().add(button3)

button4 = InlineKeyboardButton("Управление проектами", callback_data="btn4")
inline_btn4 = InlineKeyboardMarkup().add(button4)

button5 = InlineKeyboardButton("Проектная деятельность", callback_data="btn5")
inline_btn5 = InlineKeyboardMarkup().add(button5)

button_full = InlineKeyboardButton("Кнопки", callback_data="btns")
inline_btns = InlineKeyboardMarkup(row_width=1).add(button1, button2, button3, button4, button5)



