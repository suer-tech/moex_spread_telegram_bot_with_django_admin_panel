from mx.spread.calculates.calculate_spread import calculate_spread
from mx.spread.api.tickers import *
from mx.spread.api.tinkoff_api import subscribe_price
from mx.spread.models import Quote


def save_quotes(active, active_prices):
    for asset in active:
        if asset['code'] not in active:
            price = subscribe_price(asset, active_prices)
            if price is not None:
                active_prices[asset['code']] = price

    if active == usd or active == cny:
        Quote.objects.create(
            ticker=active,
            spot_price=active_prices[0].value,
            perp_price=active_prices[1].value,
            quart_price=active_prices[2].value,
            spread=0.0
        )


def save_spread(active, active_prices):
    quote_to_modify = Quote.objects.get(ticker=active)

    diff = calculate_spread(active, active_prices)
    if diff is not None:
        quote_to_modify.spread = diff
        quote_to_modify.save()


def save_quote_and_spread(active, active_prices):
    save_quotes(active, active_prices)
    save_spread(active, active_prices)


def update_quote():

    usd_prices = {}
    eur_prices = {}
    cny_prices = {}

    save_quote_and_spread(usd, usd_prices)
    save_quote_and_spread(eur, eur_prices)
    save_quote_and_spread(cny, cny_prices)