# python loop list

# loop through a list
# you can loop through out a list using a for loop
looping_lists = ['shayan','komal','sajjad','allahbakash','Kaneez fatima']
for i in looping_lists:
    print(i)
print()

# Loop Through the Index Numbers

# You can also loop through the list items by referring to their index number.
# Use the range() and len() functions to create a suitable iterable.

#printing all items by referring their index number
indexing_list_looping = ['red','green','blue','oranges']
for s in range(len(indexing_list_looping)):
    print(indexing_list_looping[s])
print()

# Using a While Loop
# You can loop through the list items by using a while loop.

# Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes.

# Remember to increase the index by 1 after each iteration.

# Example
# Print all items, using a while loop to go through all the index numbers

thislist = ["apple", "banana", "cherry"]
a = 0
while a < len(thislist):
  print(thislist[a])
  a +=1
  

