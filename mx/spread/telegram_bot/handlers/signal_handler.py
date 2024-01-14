async def generate_signal_handlers(dp, currency):
    curr_low = currency.lower()
    signal_keyboard_name = f'{curr_low}_signal_keyboard'
    signal_keyboard = locals()[signal_keyboard_name]

    @dp.message_handler(Text(equals="USD, %"))
    async def with_puree(message: types.Message):
        # Открываем клавиатуру с кнопками для управления сигналами
        await message.answer("Выберите действие:", reply_markup=signal_keyboard)

    @dp.message_handler(Text(equals="Текущий сигнал в % по USD"))
    async def current_signal_usd(message: types.Message):
        # Считываем текущий сигнал из файла и отправляем его пользователю
        try:
            with open("usd_signal.txt", "r") as file:
                signal = file.read()
                if not signal:
                    await message.answer("Текущий сигнал по USD не установлен", reply_markup=signal_keyboard)
                else:
                    await message.answer(f"Текущий сигнал в % от точки входа по USD: {signal}",
                                         reply_markup=signal_keyboard)
        except FileNotFoundError:
            await message.answer("Сигнал не найден", reply_markup=signal_keyboard)

    @dp.message_handler(Text(equals="Новый сигнал в % по USD"))
    async def new_signal_usd(message: types.Message, state: FSMContext):
        # Запрашиваем новое значение сигнала и записываем его в файл
        await message.answer("Введите новое значение сигнала в % от точки входа по USD:")
        # Устанавливаем состояние для ожидания нового значения сигнала
        await YourState.new_usd.set()

    @dp.message_handler(state=YourState.new_usd)
    async def process_new_signal(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['new_signal'] = message.text
            # Проверка, является ли введенное значение числом
            try:
                new_signal = float(data['new_signal'])
                # Сохраняем новый сигнал в файл
                with open("usd_signal.txt", "w") as file:
                    file.write(data['new_signal'])
                await message.answer(
                    f"{checkmark}Новый сигнал в % от точки входа по USD установлен: {data['new_signal']}",
                    reply_markup=signal_keyboard)
            except ValueError:
                # Если введенное значение не является числом, открываем клавиатуру
                await message.answer("Введите число")
                return  # Выходим из обработчика

        # Завершаем состояние FSMContext
        await state.finish()

    @dp.message_handler(Text(equals="Сбросить сигнал USD"))
    async def reset_usd_tvh(message: types.Message):
        usd_tvh_file = 'usd_signal.txt'

        if os.path.exists(usd_tvh_file):
            with open(usd_tvh_file, 'w', encoding='utf-8') as fw:
                pass  # Это создаст пустой файл, стирая всё содержимое
            await message.answer("Сигнал для USD сброшен.", reply_markup=signal_keyboard)
        else:
            await message.answer("Нет сохранённого сигнала.", reply_markup=signal_keyboard)