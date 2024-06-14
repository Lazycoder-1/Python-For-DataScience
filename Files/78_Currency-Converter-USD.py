
# currency converter that takes in user's currency and amount, converts it to USD
import requests

URL = 'https://v6.exchangerate-api.com/v6/6178f1d0f429513e1853a920/latest/USD'
response = requests.get(URL)
currency_data = response.json()

user_currency = input('Enter your currency: ').upper()
user_amount = int(input('Enter the amount you want to convert to USD: '))

converted_amount_USD = currency_data['conversion_rates'][user_currency] * user_amount
print('You have {} {}, That is {} USD'.format(user_amount,user_currency,converted_amount_USD))


























# def currency_convert():
#     URL = 'https://v6.exchangerate-api.com/v6/6178f1d0f429513e1853a920/latest/USD'
#     res = requests.get(URL)
#     rate = res.json()
#     USD_rate = rate['conversion_rates']
#     user_currency = str(input('Enter your currency: ')).upper()
#
#     if user_currency in USD_rate:
#         user_amount = float(input('Enter your amount: '))
#         return user_currency, USD_rate[user_currency], user_amount
#     else:
#         return None, None, None
#
# currency, rate, amount = currency_convert()
# if currency:
#     print(f'Currency found: {currency} with rate: {rate}')
#     converted_amount = amount * rate
#     print(f'Converted amount: {converted_amount}')
# else:
#     print('Enter appropriate currency')
















