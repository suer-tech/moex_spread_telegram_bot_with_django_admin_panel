async def generate_signal_only_handlers(dp, currency):
    curr_low = currency.lower()

    signal_only_keyboard_name = f'{curr_low}_signal_only_keyboard'
    signal_only_keyboard = locals()[signal_only_keyboard_name]

    @dp.message_handler(Text(equals="USD. %"))
    async def with_puree(message: types.Message):
        # Открываем клавиатуру с кнопками для управления сигналами
        await message.answer("Выберите действие:", reply_markup=signal_only_keyboard)

    @dp.message_handler(Text(equals="Текущий сигнал в % по USD."))
    async def current_signal_usd(message: types.Message):
        # Считываем текущий сигнал из файла и отправляем его пользователю
        try:
            with open("usd_signal_only.txt", "r") as file:
                signal = file.read()
                if not signal:
                    await message.answer("Текущий сигнал по USD не установлен", reply_markup=signal_only_keyboard)
                else:
                    await message.answer(f"Текущий сигнал в % по USD: {signal}", reply_markup=signal_only_keyboard)
        except FileNotFoundError:
            await message.answer("Сигнал не найден", reply_markup=signal_only_keyboard)

    @dp.message_handler(state=YourState.new_usd_only)
    async def process_new_signal(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['new_signal'] = message.text
            # Проверка, является ли введенное значение числом
            try:
                new_signal = float(data['new_signal'])
            except ValueError:
                # Если введенное значение не является числом, открываем клавиатуру
                await message.answer("Введите число")
                return  # Выходим из обработчика

            # Сохраняем новый сигнал в файл
            with open("usd_signal_only.txt", "w") as file:
                file.write(data['new_signal'])
            await message.answer(f"{checkmark}Новый сигнал в % по USD установлен: {data['new_signal']}",
                                 reply_markup=signal_only_keyboard)

        # Завершаем состояние FSMContext
        await state.finish()
        with open('usd.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()

        x = None
        for line in lines:
            if "Спред Si - USDRUBF:" in line:
                parts = line.split()
                x_index = parts.index('Спред') + 4
                x = parts[x_index]
        with open("usd_spread_only.txt", "w") as file:
            pass
            file.write(x)

    @dp.message_handler(Text(equals="Новый сигнал в % по USD."))
    async def new_signal_usd(message: types.Message, state: FSMContext):
        # Запрашиваем новое значение сигнала и записываем его в файл
        await message.answer("Введите новое значение сигнала в % по USD:")
        # Устанавливаем состояние для ожидания нового значения сигнала
        await YourState.new_usd_only.set()

    @dp.message_handler(Text(equals="Сбросить сигнал USD."))
    async def reset_usd_tvh(message: types.Message):
        usd_tvh_file = 'usd_signal_only.txt'

        if os.path.exists(usd_tvh_file):
            with open(usd_tvh_file, 'w', encoding='utf-8') as fw:
                pass  # Это создаст пустой файл, стирая всё содержимое
            await message.answer("Сигнал для USD сброшен.", reply_markup=signal_only_keyboard)
        else:
            await message.answer("Нет сохранённого сигнала.", reply_markup=signal_only_keyboard)