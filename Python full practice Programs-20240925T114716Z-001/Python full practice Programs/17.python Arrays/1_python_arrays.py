# Python Arrays
# Note: Python does not have built-in support for Arrays, but Python Lists can be used instead
# Arrays
# Note: This page shows you how to use LISTS as ARRAYS, however, to work with arrays in Python you will have to import a library, like the NumPy library.

# Arrays are use to store multiple variables in a single value
# making an array containing car names
cars = ['fortuner',"landcruiser",'Toyota Prado','Range Rover',67]


# What is an array
# An array is a special variable, which can hold more than one value at a time.
"""If you have a list of items (a list of car names, for example), storing the cars in single variables could look like this:

car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"""
# However, what if you want to loop through the cars and find a specific one? And what if you had not 3 cars, but 300?
"""The solution is an array!"""

# An array can hold many values under a single name, and you can access the values by referring to an index number.

# Access the Element of the array
x = cars[1]
print(x) # Output is landcruiser
print()

# Modifying the value of the first 
cars[1] = "Defender"
print(cars[1]) # output is Defender
print()

# The Length of an array
# use the len function to find the lenght of the array
print(len(cars)) # output is 4
print()

# Looping an array 
for items in cars:
    print(items)
print()
# output
# fortuner    
# Defender    
# Toyota Prado
# Range Rove

# Adding Array Element
# using the append() method
cars.append("civiv")
print(cars) # output ['fortuner', 'Defender', 'Toyota Prado', 'Range Rover', 'civic']
print()

# Removing array elements by index
cars.pop(4)
print(cars) # output ['fortuner', 'Defender', 'Toyota Prado', 'Range Rover']
print() 

# Removing array element by name
cars.remove("Range Rover")
print(cars) # output ['fortuner', 'Defender', 'Toyota Prado']
print() 


"""Array Methods
Python has a set of built-in methods that you can use on lists/arrays.

Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list"""
import array
int_array = array.array('i',[1,2,3,4,5,6,7,8,9])
print(int_array) 
float_array = array.array('f',[1.2,43.345,78])
print(float_array)
unicode_array = array.array('u',['s','h','a','y','a','n'])
print(unicode_array)