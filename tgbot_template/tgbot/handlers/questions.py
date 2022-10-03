from aiogram import types, Dispatcher

from ..keyboards import inline as inl


async def questions(message: types.Message):
    await message.answer("Выберите категорию", reply_markup=inl.inline_btns)


def register_questions(dp: Dispatcher):
    dp.register_message_handler(questions, commands=["Вопросы"], state="*")


