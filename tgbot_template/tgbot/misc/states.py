from aiogram.dispatcher.filters.state import StatesGroup, State


class NotificationStates(StatesGroup):
    Q1 = State()
    Q2 = State()


class Subscription(StatesGroup):
    Q1 = State()
    Q2 = State()