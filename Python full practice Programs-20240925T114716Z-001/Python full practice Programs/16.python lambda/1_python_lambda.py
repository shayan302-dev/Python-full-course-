# Python lambda

# A lambda function is a small anonymous function
# A lambda function can take any number of arguments, but can only have one expression

# The syntax of lambda
# lambda arguments: expression
# the expression is executed and the result is returned

x = lambda a : a + 10
print(x(5))# output 15
print()

# lambda function can take  any number of arguments
y = lambda s,o : s * o
print(y(5 , 3)) #output 15
print()

z = lambda l,k,j: l +k+j
print(z(5,5,5)) # output 15
print()


# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.
# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
def myfunc(n):
  return lambda a : a * n
my_doubler = myfunc(2)
my_tripler = myfunc(3)
print(my_doubler(12)) # output 24
print(my_tripler(12)) #output 36 
print()

# Use lambda functions when an anonymous function is required for a short period of time.
