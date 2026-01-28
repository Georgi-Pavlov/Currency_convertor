from currency_functions import convert_currency

while True:
    try:
        amount = float(input('Enter amount to be converted: '))
        break
    except ValueError:
        print("Invalid amount.")

from_curr = input('From currency: ').upper()
to_curr = input('To currency: ').upper()

result = convert_currency(amount, from_curr, to_curr)

if result is None:
    print('Conversion failed: unsupported currency or API error!')
else:
    print(f'{amount:.2f} {from_curr} = {result:.2f} {to_curr}')