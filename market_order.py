import ccxt

# Authorization
from api_keys import bybit_api_key, bybit_api_secret
exchange = ccxt.bybit ({
    "apiKey": bybit_api_key,
    "secret": bybit_api_secret,
    "enableRateLimit": True
})

# Order params
symbol = 'SOL/USDT:USDT'
side = "sell"
amount = 0.1

# Market order
try:
    order = exchange.create_order(symbol, 'market', side, amount)

    print("Market order created:", order)

except Exception as e:
    print("Error:", str(e))