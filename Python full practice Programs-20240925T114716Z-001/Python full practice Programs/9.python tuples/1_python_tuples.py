# Python Tuples
"""Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets."""
Im_tuple = ('hello',34,'hy',23.345,'hello')
print(Im_tuple) # ('hello', 34, 'hy', 23.345,'hello')
print()
# Remeber tuple allow duplicate values

# Tuple Items
"""Tuple items are ordered, unchangeable, and allow duplicate values.

Tuple items are indexed, the first item has index [0], the second item has index [1] etc."""
# Ordered
"""When we say that tuples are ordered, it means that the items have a defined order, and that order will not change."""

# Unchangeable
"""Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created"""

# Allow Duplicate values
"""Since tuples are indexed, they can have items with the same value:"""


# Tuple length
"""To determine how many items the tuple have we can use len() to find"""
length_tuple = ('shayan','shayan','daniyal','ahamd','daniyal')
print(len(length_tuple)) # output is 5
print()

# Create Tuple of one Item
"""To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple"""

one_item_tuple = ('shayan',) # the comma at the last is important otherwise python does not recogonized as a tuple
print(one_item_tuple) # output ('shayan',)
print(type(one_item_tuple)) # output <class tuple>
print()

# Tuple Item DataTypes
'''Tuple can be store any type of data type'''
