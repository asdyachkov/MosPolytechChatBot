from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


<<<<<<< HEAD

#Стартовая развилка
first_board = InlineKeyboardMarkup(row_width=1)
fb_buttons = [
	InlineKeyboardButton("Технологическое предпринимательство", callback_data = "b_b1"),
	InlineKeyboardButton("Ликвидация расхождений в учебных планах", callback_data = "b_b2"),
	InlineKeyboardButton("Перезачет дисциплины", callback_data = "b_b3"),
	InlineKeyboardButton("Управление проектами", callback_data = "b_b4"),
	InlineKeyboardButton("Проектная деятельность", callback_data = "b_b5")
]
for butt in fb_buttons: first_board.add(butt)



#Основы технологического предпринимательства / Технологическое предпринимательство
board1 = InlineKeyboardMarkup(row_width=1)
fb_buttons = [
	InlineKeyboardButton("У меня долг за прошлый семестр", callback_data = "b_b11"),
	InlineKeyboardButton("Как получить зачтено", callback_data = "b_b12")
]
for butt in fb_buttons: board1.add(butt)

board12 = InlineKeyboardMarkup(row_width=1)
fb_buttons = [
	InlineKeyboardButton("Когда и где пройдет пересдача?", callback_data = "b_b121"),
	InlineKeyboardButton("Как получить зачтено", callback_data = "b_b122")
]
for butt in fb_buttons: board12.add(butt)



#Управление проектами
board4 = InlineKeyboardMarkup(row_width=1)
fb_buttons = [
	InlineKeyboardButton("У меня долг за прошлый семестр", callback_data = "b_b41"),
	InlineKeyboardButton("Как получить зачтено", callback_data = "b_b42")
]
for butt in fb_buttons: board4.add(butt)

board41 = InlineKeyboardMarkup(row_width=1)
fb_buttons = [
	InlineKeyboardButton("Когда и где пройдет пересдача?", callback_data = "b_b411"),
	InlineKeyboardButton("Как получить зачтено", callback_data = "b_b412")
]
for butt in fb_buttons: board41.add(butt)



#Проектная деятельность
board5 = InlineKeyboardMarkup(row_width=1)
fb_buttons = [
	InlineKeyboardButton("Как получить зачтено", callback_data = "b_b51"),
	InlineKeyboardButton("Как узнать на какой проект я записан(а)?", callback_data = "b_b52"),
	InlineKeyboardButton("Как узнать расписание моего проекта", callback_data = "b_b53"),
	InlineKeyboardButton("Хочу поменять проект", callback_data = "b_b54"),
	InlineKeyboardButton("У меня долг за прошлый семестр", callback_data = "b_b55"),
	InlineKeyboardButton("Не назначен проект в личном кабинете", callback_data = "b_b56")
]
for butt in fb_buttons: board5.add(butt)

board52 = InlineKeyboardMarkup(row_width=1)
fb_buttons = [
	InlineKeyboardButton("Когда и где пройдет пересдача?", callback_data = "b_b521"),
	InlineKeyboardButton("Как получить зачтено", callback_data = "b_b522")
]
for butt in fb_buttons: board52.add(butt)
=======
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



>>>>>>> 97037970a2636dc9963cd07faae0d8e993d6c054
