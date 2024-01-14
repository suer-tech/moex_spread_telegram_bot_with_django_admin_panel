async def generate_sbros_handlers(dp, currency):
    curr_low = currency.lower()

    sbros_keyboard_name = f'{curr_low}_sbros_keyboard'
    sbros_keyboard = locals()[sbros_keyboard_name]

    @dp.message_handler(Text(equals="Сброс ТВХ USD"))
    async def fix_usd_tvh(message: types.Message):
        mess = 'Сбросить точку входа по USD?'
        await bot.send_message(message.chat.id, mess, reply_markup=sbros_keyboard)
