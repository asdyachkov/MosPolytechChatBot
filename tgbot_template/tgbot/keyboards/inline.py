from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# Стартовая развилка
first_board = InlineKeyboardMarkup(row_width=1)
first_board.add(
	InlineKeyboardButton("Проекты", callback_data="b_b1"),
	InlineKeyboardButton("Вопросы о текущем проекте", callback_data = "b_b2"),
	InlineKeyboardButton("Вопросы о пересдачах", callback_data="b_b3"),
	InlineKeyboardButton("Другое", callback_data="b_b4"),
)

# Проекты
project_board = InlineKeyboardMarkup(row_width=1)
project_board.add(
	InlineKeyboardButton("Технологическое предпринимательство", callback_data="b_b11"),
	InlineKeyboardButton("Управление проектами", callback_data="b_b12"),
)


#Одинаковые ответы
# Основы технологического предпринимательства / Технологическое предпринимательство
technological_enterprise = InlineKeyboardMarkup(row_width=1)
technological_enterprise.add(
	InlineKeyboardButton("У меня долг за прошлый семестр", callback_data = "b_b111"),
	InlineKeyboardButton("Как получить зачтено", callback_data = "b_b112")
)

board111 = InlineKeyboardMarkup(row_width=1)
board111.add(
	InlineKeyboardButton("Когда и где пройдет пересдача?", callback_data = "b_b1111"),
	InlineKeyboardButton("Как получить зачтено", callback_data = "b_b1112")
)
# Управление проектами
project_menejment = InlineKeyboardMarkup(row_width=1)
project_menejment.add(
	InlineKeyboardButton("У меня долг за прошлый семестр", callback_data = "b_b121"),
	InlineKeyboardButton("Как получить зачтено", callback_data = "b_b122")
)

board121 = InlineKeyboardMarkup(row_width=1)
board121.add(
	InlineKeyboardButton("Когда и где пройдет пересдача?", callback_data = "b_b1211"),
	InlineKeyboardButton("Как получить зачтено", callback_data = "b_b1212")
)



# Вопросы о текущем проекте
project_questions_board = InlineKeyboardMarkup(row_width=1)
project_questions_board.add(

	InlineKeyboardButton("Как узнать на какой проект я записан(а)?", callback_data="b_b21"),
	InlineKeyboardButton("Как получить зачтено?", callback_data="b_b22"),
	InlineKeyboardButton("Хочу поменять проект", callback_data="b_b23"),
	InlineKeyboardButton("Как узнать расписание моего проекта?", callback_data="b_b24"),
	InlineKeyboardButton("Не назначен проект в личном кабинете", callback_data="b_b25")

)


#Вопросы о пересдачах
questions_retakes = InlineKeyboardMarkup(row_width=1)
questions_retakes.add(
	InlineKeyboardButton("У меня долг за прошлый семестр", callback_data="b_b31"),
	InlineKeyboardButton("Перезачет дисциплины", callback_data = "b_b32"),
)

board31 = InlineKeyboardMarkup(row_width=1)
board31.add(
	InlineKeyboardButton("Когда и где пройдет пересдача?", callback_data = "b_b311"),
	InlineKeyboardButton("Как получить зачтено", callback_data = "b_b312")
)


#Другое
other = InlineKeyboardMarkup(row_width=1)
other.add(

	InlineKeyboardButton("Ликвидация расхождений в учебных планах", callback_data = "b_b41"),

)

#Обращение в ЦПД
board_no_ans = InlineKeyboardMarkup(row_width=1)
board_no_ans.add(
	InlineKeyboardButton("Не нашли ответа?\nОбращение в ЦПД", callback_data = "b_b1000001")
)