currencies = ["USD", "EUR", "СNY"]  # или любые другие валюты, которые вам нужны

async def generate_currencies_handlers(dp):
    for currency in currencies:
        await generate_sbros_handlers(dp, currency)
        await generate_signal_firstspread_handlers(dp, currency)
        await generate_signal_firstspread_sbros_handlers(dp, currency)
        await generate_signal_handlers(dp, currency)
        await generate_signal_only_handlers(dp, currency)
        await generate_signal_only_sbros_handlers(dp, currency)
        await generate_signal_sbros_handlers(dp, currency)
        await generate_currency_tvh_fiks_handlers(dp, currency)
        await generate_yes_no_handlers(dp, currency)






































