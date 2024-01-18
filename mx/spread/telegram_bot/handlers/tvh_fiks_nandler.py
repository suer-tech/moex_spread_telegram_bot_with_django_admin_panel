from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters import Text

from mx.spread.telegram_bot.bot import checkmark


async def generate_currency_tvh_fiks_handlers(dp, currency):
    curr_low = currency.lower()
    fiks_keyboard_name = f"{curr_low}_fiks_keyboard"
    fiks_keyboard = locals()[fiks_keyboard_name]

    @dp.message_handler(Text(equals=currency))
    async def handle_currency(message: types.Message, currency=currency):
        file_name = f'{curr_low}.txt'
        with open(file_name, 'r', encoding='utf-8') as fr:
            mess = fr.read()
            await bot.send_message(message.chat.id, mess, reply_markup=fiks_keyboard)

    @dp.message_handler(Text(equals=f"Текущая ТВХ {currency}"))
    async def current_signal(message: types.Message):
        # Считываем текущий сигнал из файла и отправляем его пользователю
        try:
            with open(f"{currency.lower()}_tvh.txt", "r") as file:
                tvh = file.read()
                if not tvh:
                    await message.answer(f"Точка входа по {currency} не установлена", reply_markup=fiks_keyboard)
                else:
                    await message.answer(f"Точка входа по {currency}: {tvh}", reply_markup=fiks_keyboard)
        except FileNotFoundError:
            await message.answer("Точка входа не найдена", reply_markup=fiks_keyboard)

    @dp.message_handler(Text(equals=f"Новая точка входа {currency} по спреду"))
    async def fix_tvh(message: types.Message):
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

                    if x is not None:
                        data_to_write = x
                        fw.write(data_to_write)
                        await message.answer(f"{checkmark}Точка входа {x} для {curr_low} зафиксирована.",
                                             reply_markup=fiks_keyboard)
                    else:
                        await message.answer(f"Не удалось найти точку входа для {curr_low}.", reply_markup=fiks_keyboard)
            else:
                await message.answer("Есть зафиксированная точка входа. Для записи новой точки сбросьте старую.",
                                     reply_markup=fiks_keyboard)
        else:
            # Файл не существует, создайте его и записывайте информацию
            with open(tvh_file, 'w', encoding='utf-8') as fw:
                with open(f'{curr_low}.txt', 'r', encoding='utf-8') as file:
                    lines = file.readlines()

                x = None
                for line in lines:
                    if f"Спред {currency}:" in line:
                        parts = line.split()
                        x_index = parts.index('Спред') + 4
                        x = parts[x_index]
                        break

                if x is not None:
                    data_to_write = x
                    fw.write(data_to_write)
                    await message.answer(f"{checkmark}Точка входа {x} для {curr_low} зафиксирована.",
                                         reply_markup=fiks_keyboard)
                else:
                    await message.answer(f"Не удалось найти точку входа для {curr_low}.", reply_markup=fiks_keyboard)

    @dp.message_handler(Text(equals=f"Запись новой точки входа {currency}"))
    async def new_signal(message: types.Message, state: FSMContext):
        # Запрашиваем новое значение сигнала и записываем его в файл
        await message.answer(f"Введите значение точки входа по {currency}:")
        # Устанавливаем состояние для ожидания нового значения сигнала
        await locals()[f'YourState.new_{curr_low}_tvh.set()']

    @dp.message_handler(state=locals()[f'YourState.new_{curr_low}_tvh.set()'])
    async def process_new_signal(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['new_signal'] = message.text

            # Сохраняем новый сигнал в файл
            with open(f"{curr_low}_tvh.txt", "w") as file:
                file.write(data['new_signal'])
            await message.answer(f"{checkmark}Новая точка входа по {currency}: {data['new_signal']}",
                                 reply_markup=fiks_keyboard)

        # Завершаем состояние FSMContext
        await state.finish()

    @dp.message_handler(Text(equals=f"Сбросить точку входа {currency}"))
    async def reset_tvh(message: types.Message):
        tvh_file = f'{curr_low}_tvh.txt'

        if os.path.exists(tvh_file):
            with open(tvh_file, 'w', encoding='utf-8') as fw:
                pass  # Это создаст пустой файл, стирая всё содержимое
            await message.answer(f"Точка входа для {currency} сброшена.", reply_markup=fiks_keyboard)
        else:
            await message.answer("Нет сохранённой точки входа.", reply_markup=fiks_keyboard)