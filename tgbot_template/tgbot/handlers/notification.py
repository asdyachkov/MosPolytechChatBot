from aiogram import types, Dispatcher
import sys, os
import re
from aiogram.dispatcher import FSMContext
from MosPolytechChatBot.tgbot_template.tgbot.misc.states import NotificationStates
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
import module_parser


async def start_notification(message: types.Message, state: FSMContext):
    await message.answer("Введите номер группы")
    await state.set_state(NotificationStates.Q1)


async def notification(message: types.Message, state: FSMContext):
    await message.answer("Секундочку)")
    if re.match("^\d{3}-\d{3,4}$", message.text):
        Zparser = module_parser.Parser(message.text)
        await message.answer(Zparser.get_next_pair())
        await state.finish()
    else:
        await message.answer("Неверная группа!")
        await state.finish()


def register_notification(dp: Dispatcher):
    dp.register_message_handler(start_notification, state=None, commands=["Пара"], commands_prefix='!/')
    dp.register_message_handler(notification, state=NotificationStates.Q1)

