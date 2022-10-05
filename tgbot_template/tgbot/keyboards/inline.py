from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



#Стартовая развилка
first_board = InlineKeyboardMarkup(row_width=1)
first_board.add(
	InlineKeyboardButton("Технологическое предпринимательство", callback_data = "b_b1"),
	InlineKeyboardButton("Ликвидация расхождений в учебных планах", callback_data = "b_b2"),
	InlineKeyboardButton("Перезачет дисциплины", callback_data = "b_b3"),
	InlineKeyboardButton("Управление проектами", callback_data = "b_b4"),
	InlineKeyboardButton("Проектная деятельность", callback_data = "b_b5")
)



#Основы технологического предпринимательства / Технологическое предпринимательство
board1 = InlineKeyboardMarkup(row_width=1)
board1.add(
	InlineKeyboardButton("У меня долг за прошлый семестр", callback_data = "b_b11"),
	InlineKeyboardButton("Как получить зачтено", callback_data = "b_b12")
)

board12 = InlineKeyboardMarkup(row_width=1)
board12.add(
	InlineKeyboardButton("Когда и где пройдет пересдача?", callback_data = "b_b121"),
	InlineKeyboardButton("Как получить зачтено", callback_data = "b_b122")
)



#Управление проектами
board4 = InlineKeyboardMarkup(row_width=1)
board4.add(
	InlineKeyboardButton("У меня долг за прошлый семестр", callback_data = "b_b41"),
	InlineKeyboardButton("Как получить зачтено", callback_data = "b_b42")
)

board41 = InlineKeyboardMarkup(row_width=1)
board41.add(
	InlineKeyboardButton("Когда и где пройдет пересдача?", callback_data = "b_b411"),
	InlineKeyboardButton("Как получить зачтено", callback_data = "b_b412")
)



#Проектная деятельность
board5 = InlineKeyboardMarkup(row_width=1)
board5.add(
	InlineKeyboardButton("Как получить зачтено", callback_data = "b_b51"),
	InlineKeyboardButton("Как узнать на какой проект я записан(а)?", callback_data = "b_b52"),
	InlineKeyboardButton("Как узнать расписание моего проекта", callback_data = "b_b53"),
	InlineKeyboardButton("Хочу поменять проект", callback_data = "b_b54"),
	InlineKeyboardButton("У меня долг за прошлый семестр", callback_data = "b_b55"),
	InlineKeyboardButton("Не назначен проект в личном кабинете", callback_data = "b_b56")
)

board55 = InlineKeyboardMarkup(row_width=1)
board55.add(
	InlineKeyboardButton("Когда и где пройдет пересдача?", callback_data = "b_b551"),
	InlineKeyboardButton("Как получить зачтено", callback_data = "b_b552")
)