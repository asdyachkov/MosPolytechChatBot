from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from tgbot.keyboards.PDbuttonsCallback import PD_callback
from tgbot.misc.states import PDStates
from tgbot.keyboards.PDbuttons import choose_course, choose_pd, choose_group_pd, choose_group_2_5_pd
from aiogram.types import CallbackQuery
import module_parser
import json
import datetime
import time


async def start_pd(message: types.Message, state: FSMContext):
    try:
        last_modified = time.strftime("%Y-%m-%d", time.strptime(time.ctime(os.path.getmtime(f"1_course.json"))))
        if str(last_modified) != str(datetime.date.today()):
            p = module_parser.ParserPD()
            p.write_data_to_json_file(p.get_data_2_5_course(), '2-5_course.json')
            p.write_data_to_json_file(p.get_data_1_course(), '1_course.json')
    except:
        p = module_parser.ParserPD()
        p.write_data_to_json_file(p.get_data_2_5_course(), '2-5_course.json')
        p.write_data_to_json_file(p.get_data_1_course(), '1_course.json')
    await message.answer("Введите Ваш курс", reply_markup=choose_course)
    await state.set_state(PDStates.W1)


async def end_pd(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await state.finish()


async def start_pd_back(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text("Введите Ваш курс", reply_markup=choose_course)
    await state.set_state(PDStates.W1)


async def theme_pd_1_course(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text("Выберите направление вашего ПД", reply_markup=choose_pd("1"))
    await state.set_state(PDStates.W2)


async def theme_pd_2_5_course(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text("Выберите направление вашего ПД", reply_markup=choose_pd("2-5"))
    await state.set_state(PDStates.W4)


async def group_pd_1_course(call: CallbackQuery, state: FSMContext):
    data = call.data
    theme = data.split(":")[1]
    await state.update_data(theme=theme)
    await call.message.edit_text("Выберите группу вашего ПД", reply_markup=choose_group_pd(theme))
    await state.set_state(PDStates.W3)


async def group_pd_1_course_back(call: CallbackQuery, state: FSMContext):
    state_data = await state.get_data()
    theme = state_data.get('theme')
    await call.message.edit_text("Выберите группу вашего ПД", reply_markup=choose_group_pd(theme))
    await state.set_state(PDStates.W3)


async def group_pd_2_5_course(call: CallbackQuery, state: FSMContext):
    data = call.data
    theme = data.split(":")[1]
    await state.update_data(theme=theme)
    await call.message.edit_text("Выберите группу вашего ПД", reply_markup=choose_group_2_5_pd(theme))
    await state.set_state(PDStates.W5)


async def group_pd_2_5_course_back(call: CallbackQuery, state: FSMContext):
    state_data = await state.get_data()
    theme = state_data.get('theme')
    await call.message.edit_text("Выберите группу вашего ПД", reply_markup=choose_group_2_5_pd(theme))
    await state.set_state(PDStates.W5)


async def output_pd_2_5_course(call: CallbackQuery, state: FSMContext):
    data = call.data
    group_id = int(data.split(":")[1])
    state_data = await state.get_data()
    theme = state_data.get('theme')
    with open("2-5_course.json", "r", encoding="utf-8") as file:
            schedule = json.load(file)

    group = [x for x in schedule[theme].keys()][group_id]
    if len(schedule[theme][group]) == 4:
        curator = schedule[theme][group][0]
        contacts = schedule[theme][group][1]
        location = schedule[theme][group][2]
        consultation = schedule[theme][group][3]
        await call.message.edit_text(f"Куратор вашего проекта: {curator}\nСвязаться с куратором: {contacts}\nВремя и место проведения ПД: {location}\nКонсультации проводятся: {consultation}")
        await state.finish()
    elif len(schedule[theme][group]) == 8:
        curator1 = schedule[theme][group][0]
        contacts1 = schedule[theme][group][1]
        location1 = schedule[theme][group][2]
        consultation1 = schedule[theme][group][3]
        curator2 = schedule[theme][group][0]
        contacts2 = schedule[theme][group][1]
        location2 = schedule[theme][group][2]
        consultation2 = schedule[theme][group][3]
        await call.message.edit_text(f"У вас на проекте 2 куратора\nПервый куратор вашего проекта: {curator1}\nСвязаться с куратором: {contacts1}\nВремя и место проведения ПД: {location1}\nКонсультации проводятся: {consultation1}\n\nВторой куратор вашего проекта: {curator2}\nСвязаться с куратором: {contacts2}\nВремя и место проведения ПД: {location2}\nКонсультации проводятся: {consultation2}")
        await state.finish()


async def output_pd_1_course(call: CallbackQuery, state: FSMContext):
    data = call.data
    group = data.split(":")[1]
    state_data = await state.get_data()
    theme = state_data.get('theme')
    with open("1_course.json", "r", encoding="utf-8") as file:
            schedule = json.load(file)
    curator = schedule[theme][group][0]
    contacts = schedule[theme][group][1]
    location = schedule[theme][group][2]    
    await call.message.edit_text(f"Куратор вашего проекта: {curator}\nСвязаться с куратором: {contacts}\nВремя и место проведения ПД: {location}")
    await state.finish()


def register_pd(dp: Dispatcher):
    dp.register_message_handler(start_pd, state=None, commands=["Расписание пд", "ПД", "пд"], commands_prefix='!/')

    dp.register_callback_query_handler(theme_pd_1_course, PD_callback.filter(choiсe="1"), state=PDStates.W1)
    dp.register_callback_query_handler(theme_pd_2_5_course, PD_callback.filter(choiсe="2-5"), state=PDStates.W1)
    dp.register_callback_query_handler(end_pd, PD_callback.filter(choiсe="back"), state=PDStates.W1)

    dp.register_callback_query_handler(start_pd_back, PD_callback.filter(choiсe="back"), state=PDStates.W2)
    dp.register_callback_query_handler(start_pd_back, PD_callback.filter(choiсe="back"), state=PDStates.W4)

    dp.register_callback_query_handler(group_pd_1_course, state=PDStates.W2)
    dp.register_callback_query_handler(group_pd_2_5_course, state=PDStates.W4)

    dp.register_callback_query_handler(theme_pd_1_course, PD_callback.filter(choiсe="back"), state=PDStates.W3)
    dp.register_callback_query_handler(theme_pd_2_5_course, PD_callback.filter(choiсe="back"), state=PDStates.W5)

    dp.register_callback_query_handler(output_pd_1_course, state=PDStates.W3)
    dp.register_callback_query_handler(output_pd_2_5_course, state=PDStates.W5)



