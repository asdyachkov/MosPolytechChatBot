import json
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from tgbot.keyboards.PDbuttonsCallback import PD_callback



choose_course = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1", callback_data=PD_callback.new(choiсe="1"))
        ],
        [
            InlineKeyboardButton(text="2-5", callback_data=PD_callback.new(choiсe="2-5"))
        ]
    ]
)




def choose_pd(course):
    if course == "1":
        with open("1_course.json", "r", encoding="utf-8") as file:
            schedule = json.load(file)
        keyboard_data = []
        for theme in schedule.keys():
            keyboard_data.append([InlineKeyboardButton(text=f"{theme}", callback_data=PD_callback.new(choiсe=f"{theme}"))])
        keyboard_data.append([InlineKeyboardButton(text='Назад ↩', callback_data=PD_callback.new(choiсe='back'))])
        return InlineKeyboardMarkup(inline_keyboard=keyboard_data)
    elif course == "2-5":
        with open("2-5_course.json", "r", encoding="utf-8") as file:
            schedule = json.load(file)
        keyboard_data = []
        for theme in schedule.keys():
            keyboard_data.append([InlineKeyboardButton(text=f"{theme}", callback_data=PD_callback.new(choiсe=f"{theme}"))])
        keyboard_data.append([InlineKeyboardButton(text='Назад ↩', callback_data=PD_callback.new(choiсe='back'))])
        return InlineKeyboardMarkup(inline_keyboard=keyboard_data)


def choose_group_pd(theme):
    with open("1_course.json", "r", encoding="utf-8") as file:
        schedule = json.load(file)
    keyboard_data = []
    for group in schedule[theme]:
        keyboard_data.append([InlineKeyboardButton(text=f"{group}", callback_data=PD_callback.new(choiсe=f"{group}"))])
    keyboard_data.append([InlineKeyboardButton(text='Назад ↩', callback_data=PD_callback.new(choiсe='back'))])
    return InlineKeyboardMarkup(inline_keyboard=keyboard_data)


def choose_group_2_5_pd(theme):
    with open("2-5_course.json", "r", encoding="utf-8") as file:
        schedule = json.load(file)
    keyboard_data = []
    for group in schedule[theme]:
        keyboard_data.append([InlineKeyboardButton(text=f"{group}", callback_data=PD_callback.new(choiсe=[x for x in schedule[theme].keys()].index(group)))])
    keyboard_data.append([InlineKeyboardButton(text='Назад ↩', callback_data=PD_callback.new(choiсe='back'))])
    return InlineKeyboardMarkup(inline_keyboard=keyboard_data)