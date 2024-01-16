async def generate_signal_firstspread_sbros_handlers(dp, currency):
    curr_low = currency.lower()

    signal_firstspread_sbros_keyboard_name = f'{curr_low}_signal_firstspread_sbros_keyboard'
    signal_firstspread_sbros_keyboard = locals()[signal_firstspread_sbros_keyboard_name]

    @dp.message_handler(Text(equals=f"Сброс сигнала по {currency}, п"))
    async def fix_tvh(message: types.Message):
        mess = f'Сбросить сигнал по {currency}?'
        await bot.send_message(message.chat.id, mess, reply_markup=signal_firstspread_sbros_keyboard)
