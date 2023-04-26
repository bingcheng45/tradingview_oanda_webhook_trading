import oandapyV20
from oandapyV20 import API
import oandapyV20.endpoints.orders as orders
import json

# Replace these with your own API credentials
api_key = "YOUR_API_KEY"
account_id = "YOUR_ACCOUNT_ID"

api = API(access_token=api_key)

def execute_order(instrument, units, side, current_price, stop_loss_pips=None, take_profit_pips=None):

    # Calculate the stop loss price
    if stop_loss_pips is not None:
        if side == "buy":
            stop_loss_price = current_price - stop_loss_pips / (100 if instrument == "USD_JPY" else 10000)
        elif side == "short":
            stop_loss_price = current_price + stop_loss_pips / (100 if instrument == "USD_JPY" else 10000)

    if take_profit_pips is not None:
        if side == "buy":
            take_profit_price = current_price + take_profit_pips / (100 if instrument == "USD_JPY" else 10000)
        elif side == "short":
            take_profit_price = current_price - take_profit_pips / (100 if instrument == "USD_JPY" else 10000)

    order_data = {
        "order": {
            "instrument": instrument,
            "units": units,
            "type": "MARKET",
            "side": side
        }
    }

    if stop_loss_pips is not None:
        order_data["order"]["stopLossOnFill"] = {
            "timeInForce": "GTC",
            "price": f"{stop_loss_price:.5f}"
        }

    if take_profit_pips is not None:
        order_data["order"]["takeProfitOnFill"] = {
            "timeInForce": "GTC",
            "price": f"{take_profit_price:.5f}"
        }

    order = orders.OrderCreate(accountID=account_id, data=order_data)
    response = api.request(order)
    print(json.dumps(response, indent=4))
