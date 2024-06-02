
#
# url = 'http://www.facebook.com'
#
# res = requests.get(url)
# print(res.content)
#

import requests
# fetching data using APIs - getting JSON data
currency_URL = "https://api.exchangerate-api.com/v4/latest/USD"
res = requests.get(currency_URL)
# get the exchange rate
rate = res.json()
print(rate['rates']['GHS'])


