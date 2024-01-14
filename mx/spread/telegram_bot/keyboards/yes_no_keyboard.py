from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


usd_yes_no_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Новая точка входа USD по спреду")).row(KeyboardButton("Запись новой точки входа USD")).row(KeyboardButton("Назад"))
eur_yes_no_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Новая точка входа EUR по спреду")).row(KeyboardButton("Запись новой точки входа EUR")).row(KeyboardButton("Назад"))
cny_yes_no_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Новая точка входа CNY по спреду")).row(KeyboardButton("Запись новой точки входа CNY")).row(KeyboardButton("Назад"))
mgnt_yes_no_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Новая точка входа MGNT по спреду")).row(KeyboardButton("Запись новой точки входа MGNT")).row(KeyboardButton("Назад"))
