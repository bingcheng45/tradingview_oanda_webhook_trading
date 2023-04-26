from flask import Flask, request, jsonify
import json
from oanda import execute_order


app = Flask(__name__)

data_history = []
trade_counter = 0

@app.route('/')
def hello_world():
    return "hello world!"

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    global data_history
    global trade_counter

    if request.method == 'POST':
        data = request.get_json()
        trade_counter += 1
        data["trade_id"] = trade_counter
        data_history.insert(0, data)  # Insert the new data at index 0
        print(json.dumps(data, indent=4))

        #extract data
        units = int(data["units"])
        # time = data["time"]
        # position = data["position"]
        instrument = data["instrument"]
        side = data["side"]
        stoploss = data.get("stoploss")
        if stoploss is not None:
            stoploss = int(stoploss)
        takeprofit = data.get("takeprofit")
        if takeprofit is not None:
            takeprofit = int(takeprofit)

        current_price = float(data["close"])
        execute_order(instrument, units, side, current_price, stoploss, takeprofit)
        return jsonify(data), 200
    elif request.method == 'GET':
        return jsonify(data_history)
