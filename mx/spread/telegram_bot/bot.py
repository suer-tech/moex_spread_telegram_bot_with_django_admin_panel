import json
import re
from datetime import datetime

import asyncio
from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.filters import Command

#
# from mx.spread.telegram_bot.currencies_handlers import generate_states_for_currencies, generate_currencies_handlers
# from mx.spread.telegram_bot.keyboards.main_keyboard import *
#
#
# from mx.spread.telegram_bot.keyboards.signal_firstspread_keyboard import signal_firstspread_keyboard
# from mx.spread.telegram_bot.keyboards.signal_keyboard import signal_keyboard
# from mx.spread.telegram_bot.keyboards.signal_only_keyboard import signal_only_keyboard

currencies = ["USD", "EUR", "СNY"]

checkmark = "✅"
token = '5814873337:AAFmEDxaPRXmg8w1HQ4FTiNB1U5l8pgtFgE'
users_id = [412850740]


current_datetime = datetime.now()


async def main():
    bot = Bot(token="TOKEN")
    dp = Dispatcher()

    await dp.start_polling(bot)


async def start_telegram_bot():
    asyncio.run(main())

#
# @dp.message(commands=['start'])
# async def process_start_command(message: types.Message):
#     mess = f'Привет, <b>{message.from_user.first_name}</b>'
#     await bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=greet_kb1)
#
# @dp.message(F.text == "Спред")
# async def with_puree(message: types.Message):
#     with open('request_pos.txt', 'w') as fw:
#         status = 'request'
#         json.dump(status, fw)
#     mess = 'Выберите актив:'
#     await bot.send_message(message.chat.id, mess, reply_markup=spread_keyboard)
#
# @dp.message(F.text == "Сигнал изменения спреда от точки входа, %")
# async def with_puree(message: types.Message):
#     # открываем файл в режиме чтения
#     mess = 'Выберите актив'
#     await bot.send_message(message.chat.id, mess, reply_markup=signal_keyboard)
#
# @dp.message(F.text == "Сигнал изменения спреда, %")
# async def with_puree(message: types.Message):
#     # открываем файл в режиме чтения
#     mess = 'Выберите актив'
#     await bot.send_message(message.chat.id, mess, reply_markup=signal_only_keyboard)
#
# @dp.message(F.text == "Сигнал изменения спреда, заданное значение")
# async def with_puree(message: types.Message):
#     # открываем файл в режиме чтения
#     mess = 'Выберите актив'
#     await bot.send_message(message.chat.id, mess, reply_markup=signal_firstspread_keyboard)
#
# @dp.message(F.text == "Главное меню")
# async def back_to_previous_menu(message: types.Message):
#     mess = 'Главное меню'
#     await bot.send_message(message.chat.id, mess, reply_markup=greet_kb1)
#
# @dp.message(F.text == "Назад")
# async def back_to_previous_menu(message: types.Message):
#     mess = 'Выберите актив:'
#     await bot.send_message(message.chat.id, mess, reply_markup=spread_keyboard)
#
# @dp.message(F.text == "Отмена")
# async def fix_usd_tvh(message: types.Message):
#     mess = 'Выберите актив'
#     await bot.send_message(message.chat.id, mess, reply_markup=signal_keyboard)
#
# @dp.message(F.text == "-Отмена-")
# async def fix_usd_tvh(message: types.Message):
#     mess = 'Выберите актив'
#     await bot.send_message(message.chat.id, mess, reply_markup=signal_firstspread_keyboard)
#
# @dp.message(F.text == "Отмена.")
# async def fix_usd_tvh(message: types.Message):
#     mess = 'Выберите актив'
#     await bot.send_message(message.chat.id, mess, reply_markup=signal_only_keyboard)
#
#
# def start_telegram_bot():
#     generate_states_for_currencies(currencies)
#     generate_currencies_handlers(dp, currencies)
#     executor.start_polling(dp)


# import telebot
# import os
# import time
# import chardet
#
# token = '6697554084:AAESe8F1SpsMwRgZa_Y5GwAX7Hf9ac6uQZ8'
# bot = telebot.TeleBot(token, parse_mode=None)
#   # Замените на свой список ID пользователей
#
# def send_message(txt_file):
#     if os.path.exists(txt_file) and os.stat(txt_file).st_size > 0:
#         encoding = detect_encoding(txt_file)
#         with open(txt_file, 'r', encoding='utf-8') as fr:
#             mess = fr.read()
#         for user in users_id:
#             try:
#                 bot.send_message(user, mess)
#             except Exception as e:
#                 print(f"Error sending message to user {user}: {e}")
#         with open(txt_file, 'w') as fw:
#             pass
#
# def detect_encoding(file_path):
#     with open(file_path, 'rb') as file:
#         result = chardet.detect(file.read())
#     return result['encoding']
#
# while True:
#     time.sleep(1)
#     send_message('sig_proc.txt')
#
# bot.polling(none_stop=True)