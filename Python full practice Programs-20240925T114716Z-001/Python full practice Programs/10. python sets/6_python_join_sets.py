# Python Join Sets

# Join Sets
# There are several ways to join two or more sets in python
"""  The Union() and update() methods join all items from both sets
     The intersection() methods keep only the duplicate items
     The difference() method keep the item form the first set that are not in the other set(s)
     The symmetric_difference() method keep all items except the duplicates items"""

# Union()
# The union() method return a new set with all items from both set
union_set1 = {1,2,3,4,5}
set5 = {11,12,13,14,15}
union_set2 = {6,7,8,9,10}
union_set3  = union_set1.union(union_set2)
union_set4 = union_set1 | union_set2
set6 = union_set1.union(union_set2,set5) # In union() you join multiple sets
"""myset = set1 | set2 | set3 |set4  you can join multiple sets in this way also"""
print(union_set3) # The output is {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(union_set4) # The output is {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(set6) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
print()
# You can use the | operator instead of the union() method, and you will get the same result.

# The union() methods can join the set with tuple
tuples = ('pakistan',"England","china")
setss = {'japan',"howkong","russia"}
joining_tuple_setss = setss.union(tuples)
print(joining_tuple_setss) # The output is unordered but successfully joined 
# Note: The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method.
print()


# Update
# The update() method inserts all items from one set into another.
# The update() changes the original set, and does not return a new set.
sets1 = {'a','b',"c"}
sets2 = {1,2,3,}
sets3 = sets1.update(sets2)
print(sets3)
print(sets1) # it output will not display because the update() changes the original set and does not return a new set
print(sets2) # {1,2,3}
print()

#  Both union() and update() will exclude any duplicate items.
excluding_set1 = {1,2,3,4}
excluding_set2 = {4,5,6,7}
excludeing = excluding_set1.union(excluding_set2)
print(excludeing) # output {1, 2, 3, 4, 5, 6, 7}
print(excluding_set1) # output {1, 2, 3, 4}
print(excluding_set2) # output {4, 5, 6, 7}
print()

# Intersection
# The Intersection keep only the duplicate items or values
# The Intersection() method will return a new set , that only contains items that are present in the both sets

Intersectioning_set1 = {'pakistan','india','afganistan',"Iran","china"}
Intersectioning_set2 = {"china","Iran","united states of america",'canada'}
Intersectioning_set3 = Intersectioning_set1.intersection(Intersectioning_set2)
print(Intersectioning_set3)  # output {'china', 'Iran'}
print()
# The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
# You can also use the & opreator instead of intersection() and you will get the same result

set45 = {"apple", "banana", "cherry"}
set46 = {"google", "microsoft", "apple"}

set47= set45 & set46
print(set47) #output {'apple'}
# Note: The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.
print() 

# The values True and 1 are considered the same value. The same goes for False and 0.
# Join sets that contains the values True, False, 1, and 0, and see what is considered as duplicates:
duplicating_set1 = {"apple", 1,  "banana", 0, "cherry"}
duplicating_set2 = {False, "google", 1, "apple", 2, True}
duplicating_set3 = duplicating_set1.intersection(duplicating_set2)
print(duplicating_set3)# output {False,1,"apple"}
print()



# Difference()
# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.

difference_set1 = {"apple", "banana", "cherry"}
difference_set2 = {"google", "microsoft", "apple"}
difference_set3 = difference_set1.difference(difference_set2)
print(difference_set3) #{"cherry","banana"}
print()

# You can use the - operator instead of the difference() method, and you will get the same result.

"""set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)"""

#Note: The - operator only allows you to join sets with sets, and not with other data types like you can with the difference() method.

# Symmetric_difference()
# The symmetric_difference() method will keep only the elements that are NOT present in both sets.
difference_symmetric_set1 = {'apple',"banana","oranges","citrus"}
difference_symmetric_set2 = {'oranges','grapes',"apple","peaches"}
difference_symmetric_set3 = difference_symmetric_set1.symmetric_difference(difference_symmetric_set2)
print(difference_symmetric_set3) # output {'banana', 'grapes', 'citrus', 'peaches'}
print()

# You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.
"""set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)"""
# Note: The ^ operator only allows you to join sets with sets, and not with other data types like you can with the symmetric_difference() method.

# symmetric_difference_update()
"""The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set instead of returning a new set."""
# Use the symmetric_difference_update() method to keep the items that are not present in both sets

symmetric_difference_update_set  = {'pakistan',"england","united states of america","dubai"}
symmetric_difference_update_set1 = {"pakistan", "england","united Kingdom","united arab emirates"}
symmetric_difference_update_set.symmetric_difference_update(symmetric_difference_update_set1)
print(symmetric_difference_update_set) # output {'united states of america', 'dubai', 'united arab emirates', 'united Kingdom'}



 
