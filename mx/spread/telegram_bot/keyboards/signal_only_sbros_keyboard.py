from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


usd_signal_only_sbros_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Сбросить сигнал USD.")).row(KeyboardButton("Отмена."))
eur_signal_only_sbros_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Сбросить сигнал EUR.")).row(KeyboardButton("Отмена."))
cny_signal_only_sbros_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Сбросить сигнал CNY.")).row(KeyboardButton("Отмена."))
mgnt_signal_only_sbros_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Сбросить сигнал MGNT.")).row(KeyboardButton("Отмена."))
