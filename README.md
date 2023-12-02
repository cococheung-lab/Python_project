# Simple Currency Converter

This script allows you to convert between different currencies using the `forex_python.converter` library by installing `pip install forex-python`

The code checks if the entered currency code of source currency and target currency are valid and a 3-letter code against the library.
If the entered code is invalid, an error message is displayed, and the user is prompted again until a valid currency code is input.

For the amount to convert, the entered amount will be checked whether it's is a valid numeric value.
If an invalid value is entered, an error message is displayed, and the user is prompted again until a valid currency code is input.

By using the convert() function from the `forex_python.converter`, when the `source_currency`, `target_currency`, and `amount` variables are passed as arguments to the function, the result will be displayed.
