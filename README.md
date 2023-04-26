# Tradingview Oanda Webhook Trading

you can host this flask app on www.pythonanywhere.com
if you like this repo, please star it and follow me on github. Thank you!

# setup
remember to replace these with your own API credentials
api_key = "YOUR_API_KEY"
account_id = "YOUR_ACCOUNT_ID"

1. create a new flask app on www.pythonanywhere.com
2. copy paste the code from `tradingview_oanda_webhook_trading.py` into the flask app
3. install oandav20 package `pip3.8 install oandav20`
4. in pythonanywhere.com, go to the web tab and modify the `WSGI configuration file:/var/www/yourUsernameHere_pythonanywhere_com_wsgi.py` and add `sys.path.append('/home/yourUsernameHere/.local/lib/python3.8/site-packages')` under the `import sys` line
5. use postman to test the webhook shown here in the url `yoursiteURL/webhook`: 

![image](https://user-images.githubusercontent.com/12640713/234690406-d978d883-7b8d-4fb7-b87a-428f72330e29.png)

6. output would be shown in the path `yoursiteURL/webhook` would look like this: 

![image](https://user-images.githubusercontent.com/12640713/234690560-55bc16d3-b8a7-4767-88e3-913ef838e519.png)

7. on trading view, create an alert and set the webhook url to `yoursiteURL/webhook` and set the alert to be sent when the condition is met via any indicator you prefer. the format is as shown:

## long
```
{
    "units": "1000",
    "time": {{time}},
    "instrument": {{ticker}},
    "side": "buy",
    "stoploss": "50", #optional
    "close": {{close}}
}
```

## short
```
{
    "units": "-1000",
    "time": "{{time}}",
    "instrument": "USD_JPY",
    "side": "short",
    "stoploss": "50", #optional
    "close": "{{close}}",
    "takeprofit": "100" #optional
}
```
