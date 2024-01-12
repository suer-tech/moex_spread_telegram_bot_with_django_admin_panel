from tinkoff.invest.services import MarketDataStreamManager

from tinkoff.invest import (
    CandleInstrument,
    Client,
    InfoInstrument,
    SubscriptionInterval,
)

from mx.spread.api.api_config import tinkoff_token


def main():
    with Client(tinkoff_token) as client:
        inst = client.instruments.find_instrument(query='MGNT')
        print(inst)
        for cur in inst.instruments:
            print(cur)
            print('')
main()