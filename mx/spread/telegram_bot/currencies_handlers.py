from mx.spread.telegram_bot.bot import currencies
from mx.spread.telegram_bot.handlers.sbros_handler import generate_sbros_handlers
from mx.spread.telegram_bot.handlers.signal_firstspread_handler import generate_signal_firstspread_handlers
from mx.spread.telegram_bot.handlers.signal_firstspread_sbros_handler import generate_signal_firstspread_sbros_handlers
from mx.spread.telegram_bot.handlers.signal_handler import generate_signal_handlers
from mx.spread.telegram_bot.handlers.signal_only_handler import generate_signal_only_handlers
from mx.spread.telegram_bot.handlers.signal_only_sbros_handler import generate_signal_only_sbros_handlers
from mx.spread.telegram_bot.handlers.signal_sbros_handler import generate_signal_sbros_handlers
from mx.spread.telegram_bot.handlers.tvh_fiks_nandler import generate_currency_tvh_fiks_handlers
from mx.spread.telegram_bot.handlers.yes_no_handler import generate_yes_no_handlers

from aiogram.dispatcher.filters.state import State, StatesGroup


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


YourState = generate_states_for_currencies(currencies)
