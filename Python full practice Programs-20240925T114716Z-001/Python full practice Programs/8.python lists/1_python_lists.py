# Python List
# The List syntax
mylist = ["apple", "banana", "cherry"]
"""List
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage

Lists are created using square brackets:"""

this_list1 = ['shayan','daniyal','sammed','sajjad']
print(this_list1) # the output is ['shayan','daniyal','sammed','sajjad']
print()

"""List Items
List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index [0], the second item has index [1] etc"""


"""Ordered
When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

If you add new items to a list, the new items will be placed at the end of the list.

Note: There are some list methods that will change the order, but in general: the order of the"""


# Changeable
# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.


# Allow Duplicates
# Since lists are indexed, lists can have items with the same value

# List allow duplicate values
this_list2 = ["shayan",'daniyal','faisal','shayan','daniyal']
print(this_list2)# The output is ["shayan",'daniyal','faisal','shayan','daniyal']
print()


# List length
# To determine how many items a list has, use the len() function:

# Print the number of items in the lists
print(len(this_list2)) # The output is 5
print() 
# the index of the len function start form 1 not 0 

# List item  - Data types
# list items can be  of any data type
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
 # The list also contain different data types
this_list3 = ['this is string',True,45,67.056,7j]
print(this_list3) # The output is ['this is string',True,45,67.056,7j]
print()

# Checking type of the list
# what is the data types of list
print(type(this_list1)) #the output is <class list>
print()