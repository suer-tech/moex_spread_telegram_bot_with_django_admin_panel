async def generate_yes_no_handlers(dp, currency):
    curr_low = currency.lower()
    yes_no_keyboard_name = f'{curr_low}_yes_no_keyboard'
    yes_no_keyboard = locals()[yes_no_keyboard_name]

    @dp.message_handler(Text(equals="Новая ТВХ USD"))
    async def fix_usd_tvh(message: types.Message):
        mess = 'Зафиксировать новую точку входа USD по спреду или вручную?'
        await bot.send_message(message.chat.id, mess, reply_markup=yes_no_keyboard)