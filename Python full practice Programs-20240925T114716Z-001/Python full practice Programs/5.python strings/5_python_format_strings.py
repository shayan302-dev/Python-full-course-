# String Formats
# As we learned in the Python variables we cannot combine string with number like this
a = 56
b = 'hello'
# print(a + b) # This generates the error

# F - strings
# we can combine strings and numbers by using the f string or format method!

"""F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations."""

print(f' My age is {a}, and {b} whats your name') # The output is My age is 56 and hello whats your name
print()


# Place holders and Modifiers
price = 56
var = f'The price of toy car is {price} dollars' # The price is place holder for the variable price
print(var) # The output is The price of toy car is 56 dollars
print()

# A place holder can include a modifier to format the value

"""A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:"""

# Display the price with 2 decimals:

var_2  = f'The price of toy car is {price:2f} dollars' # Here, .2f formats the number to two decimal places
print(var_2) # The output is The price of toy car is 56.00 dollars
print()

# A placeholder can contain Python code, like math operations:
var_3 = f'The 2 * 3 is {2*3}'
print(var_3) # The output is The 2 * 3 is 6