import os
import re
import json
import sys

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
import module_parser

from MosPolytechChatBot.tgbot_template.tgbot.misc.states import Subscription


async def subscribe(group, user_id):
    with open("subscription.json", "r") as file:
        flag = False
        subs = json.load(file)
        if group in subs.keys():
            flag = True
    with open("subscription.json", "w") as file:
        if flag:
            subs[group].append(user_id)
        else:
            subs[group] = [user_id]
        file.write(json.dumps(subs))


async def start_subscription(message: types.Message, state: FSMContext):
    await message.answer("Введите номер группы")
    await state.set_state(Subscription.Q1)


async def subscription(message: types.Message, state: FSMContext):
    if re.match("^\d{3}-\d{3,4}$", message.text.strip()):
        await message.answer("Проверяю, есть ли такая группа...")
        if module_parser.Parser(message.text).get_next_pair() != "Введена неверная группа!":
            await message.answer("Подписка подключена!)")
            await subscribe(message.text.strip(), message.from_id)
        else:
            await message.answer("Неверная группа!")
        await state.finish()
    else:
        await message.answer("Неверная группа!")
        await state.finish()


def register_subscription(dp: Dispatcher):
    dp.register_message_handler(start_subscription, state=None, commands=["Подписка"], commands_prefix='!/')
    dp.register_message_handler(subscription, state=Subscription.Q1)

