from .calculates.calculate_spread import calculate_spread
from .api.tickers import *
from .api.tinkoff_api import subscribe_price
from .models import Quote
from asgiref.sync import sync_to_async

async def save_quotes(active, active_prices):
    for asset in active:
        if asset['code'] not in active:
            price = await subscribe_price(asset, active_prices)
            if price is not None:
                active_prices[asset['code']] = price
    print(f'{active}: {active_prices}')

    if active == usd or active == cny:
        Quote.objects.create(
            ticker=active,
            spot_price=next(iter(active_prices.values())),
            perp_price=next(iter(active_prices.values())),
            quart_price=next(iter(active_prices.values())),
            spread=0.0
        )


async def save_spread(active, active_prices):
    quote_to_modify = await Quote.objects.get(ticker=active)

    diff = await calculate_spread(active, active_prices)
    if diff is not None:
        quote_to_modify.spread = diff
        await sync_to_async(quote_to_modify.save())


async def save_quote_and_spread(active, active_prices):
    await save_quotes(active, active_prices)
    await save_spread(active, active_prices)


async def update_quote():

    usd_prices = {}
    eur_prices = {}
    cny_prices = {}

    await save_quote_and_spread(usd, usd_prices)
    await save_quote_and_spread(eur, eur_prices)
    await save_quote_and_spread(cny, cny_prices)
