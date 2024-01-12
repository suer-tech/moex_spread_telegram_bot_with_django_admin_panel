# Создаем файлы под запрос пользователя о позах-----------------------------------------------------------------------------
from mx.spread.api.tickers import *
from mx.spread.models import Quote


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


def create_text_message_of_price_acrive_and_spread(active):
    quote = Quote.objects.get(ticker=active)
    if active == usd:
        quarterly = 'Si'
        perpetual = 'USDRUBF'

    if active == cny:
        quarterly = 'Cny'
        perpetual = 'CNYRUBF'

    if active == eur:
        quarterly = 'Eu'
        perpetual = 'EURRUBF'

    result = f"Спред {quarterly} - {perpetual}: {quote.spread}\n"

    if active != eur:
        spot_price = quote.spot_price
        perp_price = quote.perp_price

        if perp_price > spot_price:
            difference1 = f"{perpetual}: {'{:.3f}'.format(perp_price)} > cпот: {'{:.3f}'.format(spot_price)}\n"
        if perp_price < spot_price:
            difference1 = f"Cпот: {'{:.3f}'.format(spot_price)} > {perpetual}: {'{:.3f}'.format(perp_price)}\n"
        if '{:.3f}'.format(spot_price) == '{:.3f}'.format(spot_price):
            difference1 = f"Cпот: {'{:.3f}'.format(spot_price)} = {perpetual}: {'{:.3f}'.format(perp_price)}\n"

        result = result + difference1
    else:
        result = f"Спред {quarterly} - {perpetual}: {quote.spread}\n"

    return result
