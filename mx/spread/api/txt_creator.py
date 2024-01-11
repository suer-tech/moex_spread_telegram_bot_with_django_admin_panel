# Создаем файлы под запрос пользователя о позах-----------------------------------------------------------------------------
def createTxtFile(txt_file):
    try:
        f = open(txt_file, 'r')
    except FileNotFoundError as err:
        with open(txt_file, 'w') as fw:
            pass

# Создаем файлы для оповещения по сигналу
createTxtFile('usd_firstspread_and_signal.txt')
createTxtFile('eur_firstspread_and_signal.txt')
createTxtFile('cny_firstspread_and_signal.txt')

createTxtFile('mgnt_firstspread_and_signal.txt')


def create_text_message(currience, difference):
    if currience == usd:
        quarterly = 'Si'
        perpetual = 'USDRUBF'

    if currience == cny:
        quarterly = 'Cny'
        perpetual = 'CNYRUBF'

    if currience == eur:
        quarterly = 'Eu'
        perpetual = 'EURRUBF'

    result = f"Спред {quarterly} - {perpetual}: {difference}\n"

    if currience != eur:
        if float(second_element) > float(first_element):
            difference1 = f"{perpetual}: {'{:.3f}'.format(value_second)} > cпот: {'{:.3f}'.format(value_first)}\n"
        if float(second_element) < float(first_element):
            difference1 = f"Cпот: {'{:.3f}'.format(value_first)} > {perpetual}: {'{:.3f}'.format(value_second)}\n"
        if '{:.3f}'.format(float(second_element)) == '{:.3f}'.format(float(first_element)):
            difference1 = f"Cпот: {'{:.3f}'.format(value_first)} = {perpetual}: {'{:.3f}'.format(value_second)}\n"

        result = result + difference1
    else:
        result = f"Спред {quarterly} - {perpetual}: {difference}\n"

    return result
