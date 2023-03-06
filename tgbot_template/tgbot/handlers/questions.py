from aiogram import types, Dispatcher

from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from tgbot.keyboards import inline
#from ..keyboards import reply
from tgbot.keyboards.answer import answers

from aiogram.dispatcher import FSMContext
from tgbot.misc.states import QuestionsStates

from tgbot.cpd.ans_to_que import cpd as cdp_ids
from tgbot.cpd.ans_to_que import register_acc

async def keyboard_reply(x):
    boards = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    boards.add(
        KeyboardButton("Главное меню", callback_data="b_b0"),
        KeyboardButton("Назад", callback_data=f"b_b{x/10}")
    )
    return boards


async def CPD(message: types.Message, state: FSMContext):
    for id in cdp_ids:
        #await message.bot.send_message (id, message.text + "\n\n/" + str(message.chat.id) + '/' + str(message.message_id)) попытка Reply ответа
        await message.bot.send_message (id, message.text + "\n\n/" + str(message.chat.id))
    await state.finish()


async def start_questions(message: types.Message, state: FSMContext):
    await message.answer("Выберите категорию", reply_markup = inline.first_board)

async def questions(callback: types.CallbackQuery, state: FSMContext):
    number = int(callback.data[3:])
    
    if number == 0:
        await callback.message.edit_reply_markup(reply_markup=inline.first_board)
        await callback.message.answer("Где клавиатура?", reply_markup = ReplyKeyboardRemove)
    else:
        #await callback.message.answer("Где клавиатура?", reply_markup = keyboard_reply(number))
        if number == 1:
            await callback.message.edit_text("Проекты")
            await callback.message.edit_reply_markup(reply_markup=inline.project_board)
        elif number == 2:
            await callback.message.edit_text("Вопросы о текущем проекте")
            await callback.message.edit_reply_markup(reply_markup=inline.project_questions_board)
        elif number == 3:
            await callback.message.edit_text("Вопросы о пересдачах")
            await callback.message.edit_reply_markup(reply_markup=inline.questions_retakes)
        elif number == 4:
            await callback.message.edit_text("Другое")
            await callback.message.edit_reply_markup(reply_markup=inline.other)

        elif number == 11:
            await callback.message.edit_text("Технологическое предпринимательство")
            await callback.message.edit_reply_markup(reply_markup=inline.technological_enterprise)
        elif number == 12:
            await callback.message.edit_text("Управление проектами")
            await callback.message.edit_reply_markup(reply_markup=inline.project_menejment)

        elif number == 111:
            await callback.message.edit_text("У меня долг за прошлый семестр")
            await callback.message.edit_reply_markup(reply_markup=inline.board111)
        elif number == 121:
            await callback.message.edit_text("У меня долг за прошлый семестр")
            await callback.message.edit_reply_markup(reply_markup=inline.board121)
        elif number == 31:
            await callback.message.edit_text("У меня долг за прошлый семестр")
            await callback.message.edit_reply_markup(reply_markup=inline.board31)

        elif number == 1000001:
            await state.set_state(QuestionsStates.C1)
            await callback.message.answer("Введите ваш вопрос, он будет направлен в ЦПД")

        else:
            await callback.message.answer(answers[number], reply_markup=inline.board_no_ans)

    


def register_questions(dp: Dispatcher):
    dp.register_message_handler(start_questions, commands=["questions"], state = None, commands_prefix='!/')
    dp.register_callback_query_handler(questions, lambda callback: callback.data.startswith('b_b'), state=None)
    dp.register_message_handler(CPD, state=QuestionsStates.C1)

    register_acc(dp)