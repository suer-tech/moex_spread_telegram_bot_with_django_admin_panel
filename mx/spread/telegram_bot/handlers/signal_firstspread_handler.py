import os
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters import Text
from mx.spread.telegram_bot.bot import checkmark


async def generate_signal_firstspread_handlers(dp, currency):
    curr_low = currency.lower()

    signal_firstspread_keyboard_name = f'{curr_low}_signal_firstspread_keyboard'
    signal_firstspread_keyboard = locals()[signal_firstspread_keyboard_name]

    @dp.message_handler(Text(equals=f"{currency}, п"))
    async def with_puree(message: types.Message):
        # Открываем клавиатуру с кнопками для управления сигналами
        await message.answer("Выберите действие:", reply_markup=signal_firstspread_keyboard)

    @dp.message_handler(Text(equals=f"Текущий сигнал по {currency}, п"))
    async def current_signal_usd(message: types.Message):
        # Считываем текущий сигнал из файла и отправляем его пользователю
        try:
            tvh_file = f'{curr_low}_firstspread_and_signal.txt'

            if os.path.exists(tvh_file):
                with open(tvh_file, "r") as file:
                    data = file.read().strip()  # Убираем лишние пробелы и переводы строк

                if not data:
                    await message.answer(f"Текущий сигнал по {currency} не установлен",
                                         reply_markup=signal_firstspread_keyboard)
                else:
                    values = data.split(', ')
                    signals = values[-1]
                    if not signals:
                        await message.answer(f"Текущий сигнал по {currency} не установлен",
                                             reply_markup=signal_firstspread_keyboard)
                    else:
                        await message.answer(f"Текущий сигнал по {currency}: {signals}",
                                             reply_markup=signal_firstspread_keyboard)
        except FileNotFoundError:
            await message.answer("Сигнал не найден", reply_markup=signal_firstspread_keyboard)

    @dp.message_handler(Text(equals=f"Новый сигнал по {currency}, п"))
    async def new_signal_usd(message: types.Message, state: FSMContext):
        # Запрашиваем новое значение сигнала и записываем его в файл
        await message.answer(f"Введите новое значение сигнала по {currency}:")
        # Устанавливаем состояние для ожидания нового значения сигнала
        yourstate = f'YourState.new_{curr_low}_spread_first.set()'
        await locals()[yourstate]

    @dp.message_handler(state=locals()[f'YourState.new_{curr_low}_spread_first.set()'])
    async def process_new_signal(message: types.Message, state: FSMContext):
        tvh_file = f'{curr_low}_tvh.txt'

        if os.path.exists(tvh_file):
            # Проверьте, является ли файл пустым
            is_empty = not bool(open(tvh_file, 'r', encoding='utf-8').read())

            if is_empty:
                with open(tvh_file, 'a', encoding='utf-8') as fw:
                    with open(f'{curr_low}.txt', 'r', encoding='utf-8') as file:
                        lines = file.readlines()

                    x = None
                    for line in lines:
                        if f"Спред {currency}:" in line:
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
            with open(f"{curr_low}_firstspread_and_signal.txt", "w") as file:
                file.write(f"{x}, {data['new_signal']}")
            await message.answer(f"{checkmark}Новый сигнал по {currency} установлен: {data['new_signal']}",
                                 reply_markup=signal_firstspread_keyboard)

        # Завершаем состояние FSMContext
        await state.finish()

    @dp.message_handler(Text(equals=f"Сбросить сигнал {currency}, п"))
    async def reset_usd_tvh(message: types.Message):
        tvh_file = f'{curr_low}_firstspread_and_signal.txt'

        if os.path.exists(tvh_file):
            with open(tvh_file, 'w', encoding='utf-8') as fw:
                pass  # Это создаст пустой файл, стирая всё содержимое
            await message.answer(f"Сигнал для {currency} сброшен.", reply_markup=signal_firstspread_keyboard)
        else:
            await message.answer("Нет сохранённого сигнала.", reply_markup=signal_firstspread_keyboard)
