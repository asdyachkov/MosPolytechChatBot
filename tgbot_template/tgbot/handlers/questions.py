from aiogram import types, Dispatcher

<<<<<<< HEAD
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
=======
from ..keyboards import inline as inl


async def questions(message: types.Message):
    await message.answer("Выберите категорию", reply_markup=inl.inline_btns)


def register_questions(dp: Dispatcher):
    dp.register_message_handler(questions, commands=["Вопросы"], state="*")


>>>>>>> 97037970a2636dc9963cd07faae0d8e993d6c054
