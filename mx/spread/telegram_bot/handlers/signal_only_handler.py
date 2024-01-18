from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters import Text

from mx.spread.telegram_bot.bot import checkmark


async def generate_signal_only_handlers(dp, currency):
    curr_low = currency.lower()

    signal_only_keyboard_name = f'{curr_low}_signal_only_keyboard'
    signal_only_keyboard = locals()[signal_only_keyboard_name]

    @dp.message_handler(Text(equals=f"{currency}. %"))
    async def with_puree(message: types.Message):
        # Открываем клавиатуру с кнопками для управления сигналами
        await message.answer("Выберите действие:", reply_markup=signal_only_keyboard)

    @dp.message_handler(Text(equals=f"Текущий сигнал в % по {currency}."))
    async def current_signal(message: types.Message):
        # Считываем текущий сигнал из файла и отправляем его пользователю
        try:
            with open(f"{curr_low}_signal_only.txt", "r") as file:
                signal = file.read()
                if not signal:
                    await message.answer(f"Текущий сигнал по {currency} не установлен", reply_markup=signal_only_keyboard)
                else:
                    await message.answer(f"Текущий сигнал в % по {currency}: {signal}", reply_markup=signal_only_keyboard)
        except FileNotFoundError:
            await message.answer("Сигнал не найден", reply_markup=signal_only_keyboard)


    @dp.message_handler(state=locals()[f'YourState.new_{curr_low}_only.set()'])
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
            with open(f"{curr_low}_signal_only.txt", "w") as file:
                file.write(data['new_signal'])
            await message.answer(f"{checkmark}Новый сигнал в % по {currency} установлен: {data['new_signal']}",
                                 reply_markup=signal_only_keyboard)

        # Завершаем состояние FSMContext
        await state.finish()
        with open(f'{curr_low}.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()

        x = None
        for line in lines:
            if f"Спред {currency}:" in line:
                parts = line.split()
                x_index = parts.index('Спред') + 4
                x = parts[x_index]
        with open(f"{curr_low}_spread_only.txt", "w") as file:
            pass
            file.write(x)

    @dp.message_handler(Text(equals=f"Новый сигнал в % по {currency}."))
    async def new_signal(message: types.Message, state: FSMContext):
        # Запрашиваем новое значение сигнала и записываем его в файл
        await message.answer(f"Введите новое значение сигнала в % по {currency}:")
        # Устанавливаем состояние для ожидания нового значения сигнала
        await locals()[f'YourState.new_{curr_low}_only.set()']

    @dp.message_handler(Text(equals=f"Сбросить сигнал {currency}."))
    async def reset_tvh(message: types.Message):
        tvh_file = f'{curr_low}_signal_only.txt'

        if os.path.exists(tvh_file):
            with open(tvh_file, 'w', encoding='utf-8') as fw:
                pass  # Это создаст пустой файл, стирая всё содержимое
            await message.answer(f"Сигнал для {currency} сброшен.", reply_markup=signal_only_keyboard)
        else:
            await message.answer("Нет сохранённого сигнала.", reply_markup=signal_only_keyboard)