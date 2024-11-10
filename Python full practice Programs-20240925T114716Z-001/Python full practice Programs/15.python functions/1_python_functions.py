# Python Functions
# A function is a block of code which only runs when it is called.

# You can pass data, known as parameters, into a function.

# A function can return data as a result.


# Creating a function
# In python function is define by using def keyword
def first_function():
    print("shayan is a good boy")
# Calling a function
first_function() # output shayan is a good boy
print()


# Arguments
# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

# The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:

def second_function(name):
    print(f"{name}")
second_function("Shayan") # output Shayan
second_function("Faisal") # output Shayan
second_function("Daniyal") # output Shayan
print()
# Arguments are often shortened to args in Python documentations.

# Parameters or Arguments?
# The terms parameter and argument can be used for the same thing: information that are passed into a function.
"""From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the value that is sent to the function when it is called."""

# Number of Arguments
# By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.
def third_function(age,day):
    print(f"{age} {day}")
third_function(34,"monday") # output 34 monday
print()
# if i give more values than arguments or less value than arguments in function then we face error


# Arbitrary argument *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:

def mycars (*expensive_car):
    print("The Expensive car is :",expensive_car[2])
mycars("corolla","civic","rols royce","mercedes","bmw")
# Arbitrary Arguments are often shortened to *args in Python documentations.
print()

# Keyword Arguments
# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
print()
# The phrase Keyword Arguments are often shortened to kwargs in Python documentations.
# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

# This way the function will receive a dictionary of arguments, and can access the items accordingly

# If the number of keyword arguments is unknown, add a double ** before the parameter name:

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
# Arbitrary Kword Arguments are often shortened to **kwargs in Python documentations.
print()


# Default Parameter Value
# The following example shows how to use a default parameter value.
#  If we call the function without argument, it uses the default value:

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
print()

# Passing the list of arguments
# You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
# E.g. if you send a List as an argument, it will still be a List when it reaches the function:



cars_models = ["Toyota","Hyundai","Honda","changan","Seres","Suzuki"]
def cars_name(brand):
   for x in brand:
      print(x)

cars_name(cars_models)
print()


# Return Values
# to let the function to return a value use the return statement
def myreturn(m):
   return m + 4
print(myreturn(3))
print(myreturn(12))
# When you call myreturn(3), it calculates 3 + 4 and returns 7, but you need to use print to display it. Similarly, myreturn(12) returns 16, which also needs to be printed to be seen.
print()


# The Pass Statement
# function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
def pass_function():
   pass

# To Be Continued