from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

usd_fiks_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Текущая ТВХ USD"), KeyboardButton("Новая ТВХ USD")).row(KeyboardButton("Сброс ТВХ USD"), KeyboardButton("Назад"))
eur_fiks_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Текущая ТВХ EUR"), KeyboardButton("Новая ТВХ EUR")).row(KeyboardButton("Сброс ТВХ EUR"), KeyboardButton("Назад"))
cny_fiks_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Текущая ТВХ CNY"), KeyboardButton("Новая ТВХ CNY")).row(KeyboardButton("Сброс ТВХ CNY"), KeyboardButton("Назад"))
mgnt_fiks_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("Текущая ТВХ MGNT"), KeyboardButton("Новая ТВХ MGNT")).row(KeyboardButton("Сброс ТВХ MGNT"), KeyboardButton("Назад"))
