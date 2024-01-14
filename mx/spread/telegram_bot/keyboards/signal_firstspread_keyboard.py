from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


signal_firstspread_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton(" USD, п "), KeyboardButton(" EUR, п ")).row(KeyboardButton(" CNY, п "), KeyboardButton("MGNT, п")).row(KeyboardButton("Главное меню"))

usd_signal_firstspread_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Текущий сигнал по USD, п"), KeyboardButton("Новый сигнал по USD, п")).row(KeyboardButton("Сброс сигнала по USD, п"), KeyboardButton("-Отмена-"))
eur_signal_firstspread_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Текущий сигнал по EUR, п"), KeyboardButton("Новый сигнал по EUR, п")).row(KeyboardButton("Сброс сигнала по EUR, п"), KeyboardButton("-Отмена-"))
cny_signal_firstspread_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Текущий сигнал по CNY, п"), KeyboardButton("Новый сигнал по CNY, п")).row(KeyboardButton("Сброс сигнала по CNY, п"), KeyboardButton("-Отмена-"))
mgnt_signal_firstspread_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Текущий сигнал по MGNT, п"), KeyboardButton("Новый сигнал по MGNT, п")).row(KeyboardButton("Сброс сигнала по MGNT, п"), KeyboardButton("-Отмена-"))

