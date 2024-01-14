from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


usd_signal_firstspread_sbros_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton(" Сбросить сигнал USD, п ")).row(KeyboardButton("-Отмена-"))
eur_signal_firstspread_sbros_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton(" Сбросить сигнал EUR, п ")).row(KeyboardButton("-Отмена-"))
cny_signal_firstspread_sbros_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton(" Сбросить сигнал CNY, п ")).row(KeyboardButton("-Отмена-"))
mgnt_signal_firstspread_sbros_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton(" Сбросить сигнал MGNT, п ")).row(KeyboardButton("-Отмена-"))