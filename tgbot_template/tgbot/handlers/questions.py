from aiogram import types, Dispatcher

from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from ..keyboards import inline
#from ..keyboards import reply
from ..keyboards.answer import answers

from aiogram.dispatcher import FSMContext
from tgbot.misc.states import NotificationStates

from ..cpd.ans_to_que import cpd as cdp_ids
from ..cpd.ans_to_que import register_acc

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
        await callback.message.answer("Где клавиатура?", reply_markup = keyboard_reply(number))
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
        elif number == 55:
            await callback.message.edit_reply_markup(reply_markup=inline.board55)
        
        elif number == 1000001:
            await state.set_state(NotificationStates.Q3)
            await callback.message.answer("Введите ваш вопрос, он будет направлен в ЦПД")
        else:
            await callback.message.answer(answers[number], reply_markup=inline.board_no_ans)
    


def register_questions(dp: Dispatcher):
    dp.register_message_handler(start_questions, commands=["Вопросы"], state = "*")
    dp.register_callback_query_handler(questions, lambda callback: callback.data.startswith('b_b'), state=None)
    dp.register_message_handler(CPD, state=NotificationStates.Q3)

    register_acc(dp)