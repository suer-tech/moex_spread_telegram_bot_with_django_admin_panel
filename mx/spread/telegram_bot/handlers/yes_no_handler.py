from aiogram import Bot, types
from aiogram.dispatcher.filters import Text


async def generate_yes_no_handlers(dp, currency):
    curr_low = currency.lower()
    yes_no_keyboard_name = f'{curr_low}_yes_no_keyboard'
    yes_no_keyboard = locals()[yes_no_keyboard_name]

    @dp.message_handler(Text(equals=f"Новая ТВХ {currency}"))
    async def fix_tvh(message: types.Message):
        mess = f'Зафиксировать новую точку входа {currency} по спреду или вручную?'
        await bot.send_message(message.chat.id, mess, reply_markup=yes_no_keyboard)