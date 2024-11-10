# python sets


myset = {"apple", "banana", "cherry"}
# sets are written with curly brackets

# Set
# Sets are used to store multiple items in a single variable.

# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

# A set is a collection which is unordered, unchangeable*, and unindexed.

# * Note: Set items are unchangeable, but you can remove items and add new items.

creating_set = {'red','blue','green','yello',45,42.564}
print(creating_set) # output {'red', 'green', 'blue', 'yello', 42.564, 45}
print()
# Note: Sets are unordered, so you cannot be sure in which order the items will appear.


# Set Items
# Set items are unordered, unchangeable, and do not allow duplicate values.

# Unordered
"""Unordered means that the items in a set do not have a defined order.

Set items can appear in a different order every time you use them, and cannot be referred to by index or key."""

# Unchangele
# sets items are unchangable, meaning that we cannot change the item after the set has been create
# Note  Once a set is created you cannot change its items, but you can remove items and add new items


# Duplicate values are not allowed
# sets cannot have two items with the same value
duplicate_values_sets = {'apple','cherry','banana','apple'}
print(duplicate_values_sets) # output {'cherry', 'apple', 'banana'}
print()
# Note The True and 1 are consider duplicate values in the set and treated as duplicate

# True and 1 are consider the same value
True_1_set = {True,1,'helo','grettings','dolphin'}
print(True_1_set) # output {True, 'grettings', 'dolphin', 'helo'}
print()

# False and 0 are consider the same value  in sets, and are treated as duplicates

this_is_set = {"apple", "banana", "cherry", False, True, 0}
print(this_is_set) # output {False, True, 'banana', 'apple', 'cherry'}
print()

# Get the length of the set
print(len(this_is_set)) # output is 5
print()
# their is 6 items in the set but 0 and False are consider duplicate so the set don't count 0 and give 5


# Set items Data types
# set items can any of data types
# string int and boolean data types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
# A set can contain different data types:
# A set of int string and boolean
set4= {"abc", 34, True, 40, "male"}

# Type()
print(type(set4)) #output <class set>
print()
