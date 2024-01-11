def write_signal_to_file(signal, signal_txt):
    with open('sig_proc.txt', 'a', encoding='utf-8') as file:
        file.write(signal + '\n')
    with open(signal_txt, 'w') as file:
        pass


# Чтение значения x из файла usd_tvh.txt
def read_x_from_file(tvh_txt):
    try:
        with open(tvh_txt, 'r') as file:
            x = float(file.read())
        return x
    except FileNotFoundError:
        # Обработка случая, когда файл не найден
        return None
    except ValueError:
        # Обработка случая, когда содержимое файла не является числом
        return None


def read_firstspread_and_signal_from_file(tvh_txt):
    try:
        with open(tvh_txt, 'r') as file:
            data = file.read().split(', ')
            values = [float(value) for value in data]
            return values
    except FileNotFoundError:
        # Обработка случая, когда файл не найден
        return None
    except ValueError:
        # Обработка случая, когда содержимое файла не является числом или не может быть разделено запятой и пробелом
        return None



# Чтение значения y из файла usd_signal.txt
def read_y_from_file(signal_txt):
    try:
        with open(signal_txt, 'r') as file:
            y = float(file.read())
        return y
    except FileNotFoundError:
        # Обработка случая, когда файл не найден
        return None
    except ValueError:
        # Обработка случая, когда содержимое файла не является числом
        return None

def check_signal(curr, spread_txt, tvh_txt, signal_txt):
    with open(spread_txt, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    for line in lines:
        if "Спред" in line:
            parts = line.split()
            x_index = parts.index('Спред') + 4
            spread = parts[x_index]
    z = float(spread)  # Замените это на получение текущего значения z
    if read_x_from_file(tvh_txt) is not None and read_y_from_file(signal_txt) is not None:
        x = float(read_x_from_file(tvh_txt))  # Замените это на получение текущего значения x
        y = float(read_y_from_file(signal_txt))  # Замените это на получение текущего значения y

    # Проверяем условия и записываем сигнал, если они выполняются
        if z >= x + x / 100 * y:
            bell_emoji = "🔔"
            signal = f"{bell_emoji}{curr}: спред вырос на {y}%"
            write_signal_to_file(signal, signal_txt)
        elif z <= x - x / 100 * y:
            bell_emoji = "🔔"
            signal = f"{bell_emoji}{curr}: спред снизился на {y}%"
            write_signal_to_file(signal, signal_txt)


def check_only_signal(curr, spread_txt, signal_txt):
    with open(spread_txt, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    for line in lines:
        if "Спред" in line:
            parts = line.split()
            x_index = parts.index('Спред') + 4
            spread = parts[x_index]
    z = float(spread)  # Замените это на получение текущего значения z
    if read_firstspread_and_signal_from_file(signal_txt) is not None:
        x = read_firstspread_and_signal_from_file(signal_txt) # Замените это на получение текущего значения y


    # Проверяем условия и записываем сигнал, если они выполняются
        if float(x[0]) < float(x[1]):
            if z >= float(x[1]):
                bell_emoji = "🔔"
                signal = f"{bell_emoji}{curr}: спред вырос до {x[1]}"
                write_signal_to_file(signal, signal_txt)
        elif  float(x[0]) > float(x[1]):
            if z <= float(x[1]):
                bell_emoji = "🔔"
                signal = f"{bell_emoji}{curr}: спред снизился до {x[1]}"
                write_signal_to_file(signal, signal_txt)


check_signal('USD', 'usd.txt', 'usd_tvh.txt', 'usd_signal.txt')
check_signal('EUR', 'eur.txt', 'eur_tvh.txt', 'eur_signal.txt')
check_signal('CNY', 'cny.txt', 'cny_tvh.txt', 'cny_signal.txt')
check_signal('USD', 'usd.txt', 'usd_spread_only.txt', 'usd_signal_only.txt')
check_signal('EUR', 'eur.txt', 'eur_spread_only.txt', 'eur_signal_only.txt')
check_signal('CNY', 'cny.txt', 'cny_spread_only.txt', 'cny_signal_only.txt')
check_only_signal('USD', 'usd.txt', 'usd_firstspread_and_signal.txt')
check_only_signal('EUR', 'eur.txt', 'eur_firstspread_and_signal.txt')
check_only_signal('CNY', 'cny.txt', 'cny_firstspread_and_signal.txt')

check_signal('MGNT', 'mgnt.txt', 'mgnt_tvh.txt', 'mgnt_signal.txt')
check_signal('MGNT', 'mgnt.txt', 'mgnt_spread_only.txt', 'mgnt_signal_only.txt')
check_only_signal('MGNT', 'mgnt.txt', 'mgnt_firstspread_and_signal.txt')
