async def generate_signal_sbros_handlers(dp, currency):
    curr_low = currency.lower()
    signal_sbros_keyboard_name = f'{curr_low}_signal_sbros_keyboard'
    signal_sbros_keyboard = locals()[signal_sbros_keyboard_name]

    @dp.message_handler(Text(equals="Сброс сигнала в % по USD"))
    async def fix_usd_tvh(message: types.Message):
        mess = 'Сбросить сигнал по USD?'
        await bot.send_message(message.chat.id, mess, reply_markup=signal_sbros_keyboard)
