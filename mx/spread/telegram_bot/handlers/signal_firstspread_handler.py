async def generate_signal_firstspread_handlers(dp, currency):
    curr_low = currency.lower()

    signal_firstspread_keyboard_name = f'{curr_low}_signal_firstspread_keyboard'
    signal_firstspread_keyboard = locals()[signal_firstspread_keyboard_name]

    @dp.message_handler(Text(equals="USD, п"))
    async def with_puree(message: types.Message):
        # Открываем клавиатуру с кнопками для управления сигналами
        await message.answer("Выберите действие:", reply_markup=signal_firstspread_keyboard)

    @dp.message_handler(Text(equals="Текущий сигнал по USD, п"))
    async def current_signal_usd(message: types.Message):
        # Считываем текущий сигнал из файла и отправляем его пользователю
        try:
            usd_tvh_file = 'usd_firstspread_and_signal.txt'

            if os.path.exists(usd_tvh_file):
                with open(usd_tvh_file, "r") as file:
                    data = file.read().strip()  # Убираем лишние пробелы и переводы строк

                if not data:
                    await message.answer("Текущий сигнал по USD не установлен",
                                         reply_markup=signal_firstspread_keyboard)
                else:
                    values = data.split(', ')
                    signal = values[-1]
                    if not signal:
                        await message.answer("Текущий сигнал по USD не установлен",
                                             reply_markup=signal_firstspread_keyboard)
                    else:
                        await message.answer(f"Текущий сигнал по USD: {signal}",
                                             reply_markup=signal_firstspread_keyboard)
        except FileNotFoundError:
            await message.answer("Сигнал не найден", reply_markup=signal_firstspread_keyboard)

    @dp.message_handler(Text(equals="Новый сигнал по USD, п"))
    async def new_signal_usd(message: types.Message, state: FSMContext):
        # Запрашиваем новое значение сигнала и записываем его в файл
        await message.answer("Введите новое значение сигнала по USD:")
        # Устанавливаем состояние для ожидания нового значения сигнала
        await YourState.new_usd_spread_first.set()

    @dp.message_handler(state=YourState.new_usd_spread_first)
    async def process_new_signal(message: types.Message, state: FSMContext):
        usd_tvh_file = 'usd_tvh.txt'

        if os.path.exists(usd_tvh_file):
            # Проверьте, является ли файл пустым
            is_empty = not bool(open(usd_tvh_file, 'r', encoding='utf-8').read())

            if is_empty:
                with open(usd_tvh_file, 'a', encoding='utf-8') as fw:
                    with open('usd.txt', 'r', encoding='utf-8') as file:
                        lines = file.readlines()

                    x = None
                    for line in lines:
                        if "Спред Si - USDRUBF:" in line:
                            parts = line.split()
                            x_index = parts.index('Спред') + 4
                            x = parts[x_index]
                            break

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
            with open("usd_firstspread_and_signal.txt", "w") as file:
                file.write(f"{x}, {data['new_signal']}")
            await message.answer(f"{checkmark}Новый сигнал по USD установлен: {data['new_signal']}",
                                 reply_markup=signal_firstspread_keyboard)

        # Завершаем состояние FSMContext
        await state.finish()

    @dp.message_handler(Text(equals="Сбросить сигнал USD, п"))
    async def reset_usd_tvh(message: types.Message):
        usd_tvh_file = 'usd_firstspread_and_signal.txt'

        if os.path.exists(usd_tvh_file):
            with open(usd_tvh_file, 'w', encoding='utf-8') as fw:
                pass  # Это создаст пустой файл, стирая всё содержимое
            await message.answer("Сигнал для USD сброшен.", reply_markup=signal_firstspread_keyboard)
        else:
            await message.answer("Нет сохранённого сигнала.", reply_markup=signal_firstspread_keyboard)