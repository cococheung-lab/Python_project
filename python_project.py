import forex_python.converter as c

# Get the listed currency on forex_python
listed_currency = c.get_rates('').keys()

# Check if the source currency is valid
while True:
        source_currency = input("Enter the source currency code (e.g., AUD, HKD): ").upper()