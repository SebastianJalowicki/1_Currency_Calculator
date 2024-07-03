# Kalkulator Walut / Currency Calculator

import requests


def get_exchange_rate(currency_code, date):
    url = f"http://api.nbp.pl/api/exchangerates/rates/a/{currency_code}/{date}/?format=json"
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    data = response.json() 
    exchange_rate = data['rates'][0]['mid']
    return exchange_rate

# Main program

print('CURRENCY CALCULATOR | KALKULTOR WALUT')

currency_code = input('Enter currency code (e.g. EUR): ')
date = input('Enter date (YYYY-MM-DD): ')
rate = get_exchange_rate(currency_code, date)

if rate:
    print(f'Exchange rate for 1 {currency_code.upper()} = {rate} PLN on {date}.')
else:
    print('Invalid currency code or date.')