import forex_python.converter as c

listed_currency = c.get_rates('').keys()

while True:
    source_currency = input("Enter the source currency code (e.g., AUD, HKD): ").upper()
    if len(source_currency) == 3 and source_currency in listed_currency:
        break
    else:
        print("Invalid source currency code. Please enter a valid 3-letter currency code.")

while True:
    target_currency = input("Enter the target currency code (e.g., AUD, HKD): ").upper()
    if len(target_currency) == 3 and target_currency in listed_currency:
        break
    else:
        print("Invalid target currency code. Please enter a valid 3-letter currency code.")

while True:
    try:
        amount = float(input("Enter the amount to convert: "))
        break
    except ValueError:
        print("Invalid amount. Please enter a valid numeric value.")

result = c.convert(source_currency, target_currency, amount)
print(result)
