import os
import requests

headers = {
    'Content-Type': 'application/json'
}

token = os.getenv('TIINGO_KEY')
# Barrick - GOLD
# Golden Start resources - GSS
ticker = 'GSS'

requestResponse = requests.get(f"https://api.tiingo.com/iex/?tickers={ticker},spy&token={token}", headers=headers)
print(requestResponse.json()[0])
