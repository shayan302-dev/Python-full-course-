# Python access  set items

# Access items
# you cannot access items in a set  by refering an index or key
# but you can loop through a set items using  a for loop, or ask a specified item present in set, by using in keyword

looping_sets = {1,4j,9.89,'yes',True}
for i in looping_sets:
    print(i)
print()
# To check if a 1 is present in the set 
if 1 in looping_sets:
    print('yes it is in the set') # yes it is in the set
print()

# using the keyword not in
if 89 not in looping_sets:
    print("yes it is not in the set") # yes it is not in the set
print()

# Change items
# once a set is crated you can not change the items but you can add the new items

