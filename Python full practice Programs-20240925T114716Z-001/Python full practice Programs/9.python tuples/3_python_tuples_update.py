# Python Items Update

#Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.

# But there are some workarounds.

# Change Tuple Values
""""Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple."""

# Convert the tuple into a list to be able to change it:

tuple2 = ('hello','fruits','greetings','air cooler')
converting_tuple_to_list = list(tuple2)
converting_tuple_to_list[0] = 'hy'
tuple2 = tuple(converting_tuple_to_list)
print(tuple2) # output ('hy', 'fruits', 'greetings', 'air cooler')
print()

# Add Items
"""Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.

1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple"""

# Convert the tuple into a list, add "orange", and convert it back into a tuple
tuple3 = ('red','green','blue','oranges','skyblue')
again_converting_tuple_into_list = list(tuple3)
again_converting_tuple_into_list.append('navy blue')
tuple3 = tuple(again_converting_tuple_into_list)
print(tuple3)# output ('red', 'green', 'blue', 'oranges', 'skyblue', 'navy blue')
print()


# Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:

tuple4 = ('fazeen','ayesha','komal','kashaf')
tuple5 = ('rabia',)
tuple4 +=tuple5
print(tuple4) # output ('fazeen', 'ayesha', 'komal', 'kashaf', 'rabia')
print()
# Note: When creating a tuple with only one item, remember to include a comma after the item, otherwise it will not be identified as a tuple

# Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:

tuple6 = ('mithu','murga','bahadur Murgi','choti murgi','khala ka mithu')
y = list(tuple6)
y.remove('khala ka mithu')
tuple6 = tuple(y)
print(tuple6) # output ('mithu', 'murga', 'bahadur Murgi', 'choti murgi')
print()


# The del keyword can delete the tuple completely:

thistuple = ("apple", "banana", "cherry")
del thistuple
# print(thistuple) #this will raise an error because the tuple no longer exists