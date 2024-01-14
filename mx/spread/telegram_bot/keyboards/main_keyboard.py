from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_spread = KeyboardButton("Спред")
button_set_proc_tvh = KeyboardButton("Сигнал изменения спреда от точки входа, %")
button_set_proc = KeyboardButton("Сигнал изменения спреда, %")
button_set = KeyboardButton("Сигнал изменения спреда, заданное значение")

greet_kb1 = ReplyKeyboardMarkup(resize_keyboard=True).row(button_spread).row(button_set_proc_tvh).row(button_set_proc).row(button_set)
spread_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True).add(KeyboardButton("USD"), KeyboardButton("EUR")).row(KeyboardButton("CNY"), KeyboardButton("MGNT")).row(KeyboardButton("Главное меню"))










