# Python Numbers
 # There are three types of numeric data types in python
int 
float 
complex 

# Example of above data types
a = 34 
b = 3.4
c = 3+4j
print(a,'This is int data type')
print(b,'This is float data type')
print(c,'This is complex data type')
print()
# You can verify their types using the type function in the python

# Int
# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length

i1 = 1234567890
i2 = -23234234232
i3 = 1
print(type(i1))
print(type(i2))
print(type(i3))
print()

# Float
# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

f1 = 1.121
f2 = -3.234
f3 = 1.0
print(type(f1))
print(type(f2))
print(type(f3))
# Float can also be scientific numbers with an "e" to indicate the power of 10.
f4 = 2.4e54 # This is the float
print(type(f4))
print()

# Complex
# Complex numbers are written with a "j" as the imaginary part
c1 = 3+6j
c2 = 4j
c3 = -4j
print(type(c1))
print(type(c2))
print(type(c3))
print()

# Type Conversion
# You can convert from one type to another with the int(), float(), and complex() methods:

conversion1 = 34
conversion2 = 3.5
conversion3 = 1j
# converting int to float
C1 = float(conversion1)
# converting float to int
C2 = int(conversion2)
# converting int to complex
C3 = complex(conversion1)
print(C1)
print(C2)
print(C3)
# now using the type function to see their types
print(type(C1))
print(type(C2))
print(type(C3))
print()
# Note complex can't convert to the other data type but other data types can convert in to the complex

# Random
# Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:

import random # it is built in module in the python
print(random.randrange(1,10)) # Every times its run it will print one number from 1 to 10