from currency_converter import CurrencyConverter

def convert_currency(amount, base_currency, target_currency):
    c = CurrencyConverter()
    result = c.convert(amount, base_currency, target_currency)
    return result

amount = float(input('Enter the amount to convert: '))
base_currency = input('Enter the base currency: ').upper
target_currency = input('Enter the target currency: ').upper

# perform the convertion
convert_amount = convert_currency(amount, base_currency, target_currency)
print(f'{amount} {base_currency} = {convert_amount}{target_currency}')