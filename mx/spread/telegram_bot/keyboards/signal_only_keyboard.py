from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


signal_only_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("USD. %"), KeyboardButton("EUR. %")).row(KeyboardButton("CNY. %"), KeyboardButton("MGNT. %")).row(KeyboardButton("Главное меню"))

usd_signal_only_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Текущий сигнал в % по USD."), KeyboardButton("Новый сигнал в % по USD.")).row(KeyboardButton("Сброс сигнала в % по USD."), KeyboardButton("Отмена."))
eur_signal_only_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Текущий сигнал в % по EUR."), KeyboardButton("Новый сигнал в % по EUR.")).row(KeyboardButton("Сброс сигнала в % по EUR."), KeyboardButton("Отмена."))
cny_signal_only_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Текущий сигнал в % по CNY."), KeyboardButton("Новый сигнал в % по CNY.")).row(KeyboardButton("Сброс сигнала в % по CNY."), KeyboardButton("Отмена."))
mgnt_signal_only_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Текущий сигнал в % по MGNT."), KeyboardButton("Новый сигнал в % по MGNT.")).row(KeyboardButton("Сброс сигнала в % по MGNT."), KeyboardButton("Отмена."))

