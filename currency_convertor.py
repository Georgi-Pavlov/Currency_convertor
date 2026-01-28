from currency_functions import convert_currency

amount_ = float(input('Enter amount to be converted: '))
from_curr = input('From currency to convert: ')
to_curr = input('To currency to convert: ')
converted = convert_currency(amount_, from_curr, to_curr)
print(f'{amount_} {from_curr} = {converted} {to_curr}')
