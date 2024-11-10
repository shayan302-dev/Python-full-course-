# Python For Loops
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).


# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
# Example
# iterating a list
bussiness = ["Wholesale","forestry","real estate","Trading"]
for i in bussiness:
    print(i)
print()
# The for loop does not require an indexing variable to set beforehand.


# Looping Through a String
# we can iterate a string because string contains characters
iterating_string = "Shayan"
for s in iterating_string:
    print(s)
print()


# The Break Statement
# The break statement in a Python for loop is used to exit the loop prematurely when a certain condition is met. It stops the loop execution and moves the control to the first statement following the loop. This helps in optimizing performance by avoiding unnecessary iterations.

technologies = ["Cloud computing","Machine learning","Data Mining","Web Scraping","natural language processing"]
for t in technologies:
    print(t)
    if t == "Data Mining":
        break
    print(t)
print()

# The Continue Statement
# The continue statement in Python is used within loops to skip the current iteration and move to the next one. When encountered, it bypasses the remaining code inside the loop for that iteration. This helps in controlling loop execution flow based on specific conditions.

books = ["Rich dad poor dad",'Fake Money',"Hands On Machine Learning Keras Scikit Learn and TensorFlow","The Real Book of Real Estate","Cashflow Quadrant"]
for b in books:
    if b == "Hands On Machine Learning Keras Scikit Learn and TensorFlow":
        continue
    print(b)
print()


# The Range Function
# To loop through a set of code a specified number of times, we can use the range() function 

# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

# Example
for r in range(1,10): # 1 and 10 are called the parameters or arguments both terms can be use 
    print(r) # it will print form 1 to 9
print()
# note range(10) will print form value 0 to 9 and if we range(1,10) then 1 to 9


# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
for n in range(1,10,2): # 1 is start 10 is stop and 2 is step
    print(n) # The output is 1 3 5 7 9
print()


# Else in For Loop
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
for g in range(6):
    print(g)
else:
    print("loop finished")

#  The else block will NOT be executed if the loop is stopped by a break statement.
for e in range(6):
    if e == 4:
        break
    print(e)
else:
    print("loop finished")



# Nested Loop
# A loop inside a loop is called a nested loop
colors = ["red","yellow","green"]
fruits = ['Apple',"banana","citrus"]
for x in colors:
    for y in fruits:
        print(x,y)
print()


# The pass statement
# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
for k in range(100):
    pass
