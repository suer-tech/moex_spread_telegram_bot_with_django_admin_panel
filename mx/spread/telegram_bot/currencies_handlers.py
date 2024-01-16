async def generate_currencies_handlers(dp, currencies):
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


def generate_states_for_currencies(currencies):
    class YourState(StatesGroup):
        pass

    for currency in currencies:
        state_name = f"new_{currency.lower()}"
        only_state_name = f"new_{currency.lower()}_only"
        tvh_state_name = f"new_{currency.lower()}_tvh"
        spread_first_state_name = f"new_{currency.lower()}_spread_first"

        setattr(YourState, state_name, State())
        setattr(YourState, only_state_name, State())
        setattr(YourState, tvh_state_name, State())
        setattr(YourState, spread_first_state_name, State())

    return YourState

# Пример использования:

YourState = generate_states_for_currencies(currencies)
