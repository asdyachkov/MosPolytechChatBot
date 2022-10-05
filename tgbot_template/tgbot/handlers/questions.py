from aiogram import types, Dispatcher
from ..keyboards import inline
from ..keyboards.answer import answers

async def start_questions(message: types.Message):
    await message.answer("Выберите категорию", reply_markup = inline.first_board)

async def questions(callback: types.CallbackQuery):
    number = int(callback.data[3:])
    await callback.message.answer("Ответ")

    if number == 1:
        await callback.message.edit_reply_markup(reply_markup=inline.board1)
    elif number == 4:
        await callback.message.edit_reply_markup(reply_markup=inline.board4)
    elif number == 5:
        await callback.message.edit_reply_markup(reply_markup=inline.board5)
    elif number == 12:
        await callback.message.edit_reply_markup(reply_markup=inline.board12)
    elif number == 41:
        await callback.message.edit_reply_markup(reply_markup=inline.board41)
    elif number == 52:
        await callback.message.edit_reply_markup(reply_markup=inline.board52)
    else:
        text = answers[number]
        await callback.message.answer(text)

    await callback.message.answer("Ответ")
    


def register_questions(dp: Dispatcher):
    dp.register_message_handler(start_questions, commands=["Вопросы"], state = "*")
    dp.register_callback_query_handler(questions, lambda callback: callback.data.startswith('b_b'))