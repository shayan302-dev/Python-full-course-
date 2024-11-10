# Change  Item Value
# To change the value of the specific item in the list refer to the index numbers

# In this we change the second item
changing_list_item = ['Corolla','Civic','Elantra','Sportage',"Alsiven"]
changing_list_item[1]  = 'Hyundai Sonata'
print(changing_list_item) # output ['Corolla', 'Hyundai Sonata', 'Elantra', 'Sportage', 'Alsiven']
print()

# Changing a range of Item Values
#To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:

# changing the value of the surf excel , harpic and shampoo
changing_range_of_items_of_lists = ['Surf excel','Harpic',"Shampoo", "soap",'dishwasher soap']

changing_range_of_items_of_lists[0:3] = ["Ariel","phenail",'Head & shoulders']

print(changing_range_of_items_of_lists)# output ['Ariel', 'phenail', 'Head & shoulders', 'soap', 'dishwasher soap']
print()

# If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

# Change the second value by replacing it with two new values:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist) # output ['apple', 'blackcurrant', 'watermelon', 'cherry']
print()


# insert items
# To insert a new item without replacing any item of the string we use the insert() method

# The insert() method inserts an item at the specified index:
list = ['Red','Green','Blue','Orange']
list.insert(2,'Yello')
print(list) # output ['Red', 'Green', 'Yello', 'Blue', 'Orange']