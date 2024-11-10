        # Global variables
# Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables. Global variables can be used by everyone, both inside of functions and outside.

# Create a variable outside of a function, and use it inside the function
x = 'helloworld'
def myfunction():
    print('python is ' + x)
myfunction()
print()

# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.
y = 'This is the global variable' # This is the global variable
def function():
    y = 'This is inside the variable function' # This is the local variable
    print(y)
function() # This function print the "This is insude the variable function"
print(y) # This print  This is the global variable'
print()
# Global Keyword
def globalvar():
    global a
    a = 'This is the local vairable inside the function which  turns in to golbal using the global keyword'
globalvar()
print(a)
print()



# To change the value of a global variable inside a function, refer to the variable by using the global keyword:

v = 'shayan'
def changing_global_var_inside_function():
    global v
    v = 'Ayan'
    print(v)
changing_global_var_inside_function()
print(v)