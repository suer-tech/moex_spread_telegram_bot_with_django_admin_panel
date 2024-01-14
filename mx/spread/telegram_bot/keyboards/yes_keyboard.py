from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


usd_yes_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Зафиксировать точку входа по USD")).row(KeyboardButton("Назад"))
eur_yes_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Зафиксировать точку входа по EUR")).row(KeyboardButton("Назад"))
cny_yes_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Зафиксировать точку входа по CNY")).row(KeyboardButton("Назад"))
mgnt_yes_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Зафиксировать точку входа по MGNT")).row(KeyboardButton("Назад"))

