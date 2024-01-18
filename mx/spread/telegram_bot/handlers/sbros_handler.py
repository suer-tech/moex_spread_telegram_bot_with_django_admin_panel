from aiogram import Bot, types
from aiogram.dispatcher.filters import Text
from mx.spread.telegram_bot.bot import bot


async def generate_sbros_handlers(dp, currency):
    curr_low = currency.lower()

    sbros_keyboard_name = f'{curr_low}_sbros_keyboard'
    sbros_keyboard = locals()[sbros_keyboard_name]

    @dp.message_handler(Text(equals=f"Сброс ТВХ {currency}"))
    async def fix_tvh(message: types.Message):
        mess = f'Сбросить точку входа по {currency}?'
        await bot.send_message(message.chat.id, mess, reply_markup=sbros_keyboard)
