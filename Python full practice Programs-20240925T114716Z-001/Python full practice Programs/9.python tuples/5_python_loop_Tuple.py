# Python Loop Tuple

# Loop through a tuple
# You can loop through the tuple items by using a for loop.
mytuple = ('hello','hy','car','areoplane','rockets','spaceships','bombs')
for i in mytuple:
    print(i)
print()
    # output
# hello
# hy        
# car       
# areoplane 
# rockets   
# spaceships
# bombs


# Loop Through the Index Numbers
"""You can also loop through the tuple items by referring to their index number.

Use the range() and len() functions to create a suitable iterable.""" 

hellotuple=  ('kiwi','peach','oranges','Manoges')
for s in range(len(hellotuple)):
    print(hellotuple[s])
print()


# Using a While Loop
# You can loop through the tuple items by using a while loop.

# Use the len() function to determine the length of the tuple, then start at 0 and loop your way through the tuple items by referring to their indexes.

# Remember to increase the index by 1 after each iteration.

# Example
# Print all items, using a while loop to go through all the index numbers:

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
