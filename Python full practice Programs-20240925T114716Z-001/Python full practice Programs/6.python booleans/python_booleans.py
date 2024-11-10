# python booleans
# boolean represents the one or two values True and False

# Boolean Values
# In programming you often need to know if an expression is True and False.
# you can evaluate any expression in python , and get the two answers True and False.
# when you compare two values, the expression is evaluated and python returns boolean answers

print( 10 > 8) # returns True because 10 is greater than 8
print(10 == 8) # returns False because 10 is not equal to 8
print( 10 < 8) # returns False because 10 is greater than 8
print()# This is for space 

# When you run a condition in an if statement, Python returns True or False:

# print a condition based on weather the condition is True or False:
a = 89
b = 33
if b > a:
    print('b is greater than a')
else:
    print('a is greater than b')
print()

# Evaluate Values and Variables
#  The bool() allows you to evaluate any value , give you True or False
# Evaluate  a string and number

print(bool('This is the string ')) # returns True because it is string
print(bool(34)) # return True because it is an integer
print()
# Evaluating the two variables
c = 'hello'
v = 45
print(bool(c)) # returns True
print(bool(a)) # returns True
print()


"""Most Values are True
Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones."""

# The following will return True
print(bool(67)) # return True
print(bool('This is a string')) # return True
print(bool(["This","is","List" ])) # return True
print()


"""Some Values are False
In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False."""

# bool(False)
# bool(None)
# bool(0)
# bool("")
# bool(())
# bool([])
# bool({})



# Function return True
#  you can create a function which can return True
def ReturnTrue():
    return True
print(ReturnTrue())
# Return True