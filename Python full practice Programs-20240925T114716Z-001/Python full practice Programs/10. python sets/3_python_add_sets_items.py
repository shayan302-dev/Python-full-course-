# Python Add Set items
# ADD Items
# Once a set is created, you cannot change its items, but you can add new items.
# to add one item in to the set use the add() method
adding_item_in_set = {"red",'Green',"pakisatn"}
adding_item_in_set.add("saudia arabia") # The add() method takes one argument only
print(adding_item_in_set) # The results are changed everytime when run the program because the sets are unordered
print()

# To add items from another set into the current set, use the update() method.
set1 = {'pakistan','USA',"china","india",'australia','greenland'}
set2 = {'japan',"southkorea","Russia","dubai","abu dahbi","egypt"}
set1.update(set2)
print(set1) # it successfully add items from one set to another set
print()

# ADD any iterable
# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
set3 = {"water","coca cola","sprite"}
list1 = ['pakoala',"gourmet","cola next"]
set3.update(list1)
print(set3) # it successfully add items from the list1 to set3 
print()