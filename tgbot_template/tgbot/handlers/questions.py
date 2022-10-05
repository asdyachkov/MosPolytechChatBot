from aiogram import types, Dispatcher

from ..keyboards import inline


async def start_questions(message: types.Message):
    await message.answer("Выберите категорию", reply_markup = inline.first_board)

async def questions(callback: types.CallbackQuery):
    v = int(callback.data[3:])

    # сопоставление кнопки и ответа
    #....

    await callback.answer(text = f"I work{v}")


def register_questions(dp: Dispatcher):
    dp.register_message_handler(start_questions, commands=["Вопросы"], state = "*")
    dp.register_callback_query_handler(questions, lambda callback: callback.data.startswith('b_b'))