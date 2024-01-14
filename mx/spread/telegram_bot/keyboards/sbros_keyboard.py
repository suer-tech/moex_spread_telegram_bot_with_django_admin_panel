from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

usd_sbros_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Сбросить точку входа USD")).row(KeyboardButton("Назад"))
eur_sbros_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Сбросить точку входа EUR")).row(KeyboardButton("Назад"))
cny_sbros_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Сбросить точку входа CNY")).row(KeyboardButton("Назад"))
mgnt_sbros_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Сбросить точку входа MGNT")).row(KeyboardButton("Назад"))
