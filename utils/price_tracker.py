import requests

def get_btc_price():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": "bitcoin", "vs_currencies": "usd"}
    try:
        response = requests.get(url, params=params)
        return response.json()["bitcoin"]["usd"]
    except:
        return "Unavailable"
