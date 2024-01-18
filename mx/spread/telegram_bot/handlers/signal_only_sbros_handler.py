from aiogram import Bot, types
from aiogram.dispatcher.filters import Text
from mx.spread.telegram_bot.bot import bot


async def generate_signal_only_sbros_handlers(dp, currency):
    curr_low = currency.lower()

    signal_only_sbros_keyboard_name = f'{curr_low}_signal_only_sbros_keyboard'
    signal_only_sbros_keyboard = locals()[signal_only_sbros_keyboard_name]

    @dp.message_handler(Text(equals=f"Сброс сигнала в % по {currency}."))
    async def fix_tvh(message: types.Message):
        mess = f'Сбросить сигнал по {currency}?'
        await bot.send_message(message.chat.id, mess, reply_markup=signal_only_sbros_keyboard)
