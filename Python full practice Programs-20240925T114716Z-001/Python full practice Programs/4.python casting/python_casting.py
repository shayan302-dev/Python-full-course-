"""Specify a Variable Type
There may be times when you want to specify a type on to a variable. This can be done with casting. Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

Casting in python is therefore done using constructor functions:

int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)

float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)

str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals"""

# Integers

i1 = int(23) # this print 23 because this is integer
i2 = int(2.8) # this is float but we cast it in to integer this print 2
i3  = int('4') # this is in string but we cast it in to integer it print 4
print(i1)
print(i2)
print(i3)
print(type(i1))
print(type(i2))
print(type(i3))
print()
# you cannot convert the string in to int if the string is in alphnumeric or alphabets


# Floats

f1 = float(23)# this print 2.30
f2 = float (4.45) # this print 4.45
f3 = float('4') # this print 4.0
f4 = float('6.75') # this print 6.75
print(f1)
print(f2)
print(f3)
print(f4)
print(type(f1))
print(type(f2))
print(type(f3))
print(type(f4))
print()

# Strings
s1 = str(45) # This print "45" 
s2 = str('t54') # This print 't54'
s3 = str(3.0) # This print "3.0"
print(s1) 
print(s2) 
print(s3)
print(type(s1)) 
print(type(s2)) 
print(type(s3)) 
# Note The compelx data type cannot cast in to other data type

