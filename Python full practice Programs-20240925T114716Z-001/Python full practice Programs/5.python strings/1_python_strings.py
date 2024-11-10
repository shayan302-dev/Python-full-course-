# string in the python can me either single or double quotation mark 'hello',"hello"
print('hello')# This is the string 
print("hello")# This is the string
print('''Hello 
      how are
      you''') # This is also string


'''The triple quotes can't give error if they use without print() function the python interpreter igonores these lines in triple quotes so we can use it like a comment but official it is not comment'''
print()

#Quotes inside the Quotes
# you can use quotes inside the string,as long as long they don't match the qoutes surrounding the string

print('Hello this is "Shayan"')# This print Hello this is "Shayan"
print("Hello this is 'Shayan'")# This print Hello this is 'Shayan'
print( """ hello this 'shayan'""") # this print hello this is 'shayan'
# print('Hello this is 'shayan'')# This give the error
# print("Hello this is "shayan"")# This give the error

# Assigning String to a variable
s = 'hello to all the world'
print(s) # This print hello to all the world 
print()

# Multiline strings
# you can assign a multiline string to a variable using three quotes
b = """ shayan is a good boy
and he is a intelligent boy
he is good in sports and in coding
shayan love coding""" # You can also use the """""" doubles quotes three time instead of '''''' single quotes
print(b) # as same sequence will print this is the benefit of the three quotes string 
print()

# Strings are Arrays

# Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.
v = 'hello shayan'
print(v[1]) # the output is e
print()
# its indexing start from 0

# Loop Through a string
x = 'shayan'
for shayan in x:
    print(shayan)# its output is vertical s h a y a n
print()

# String length
# you can use the len()function to measure the length of the string
x1 = 'shayan'
print(len(x)) # it output is 6
print()
# its indexing start from 1

# Check String
# to check if certain phrase or word is in the string it return in bool like true or false
x3 = 'shayan is a good boy'
print('shayan' in x3 ) #returns ture
print('hello' not in x3) # returns true
if 'boy' in x3: # it will only execute if boy is in the x3 otherwise not and you can also check in this way
    print('yes it is in x3')
if "yes" not in x3: # will print it is not in the x3 which is true
    print('it is  not in the x3') #
print()