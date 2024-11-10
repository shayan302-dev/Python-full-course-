# Remove Specified Item
# the remove() remove the specified item in the list
removing_item_in_list = ['hello','hy','salam','wsalam']
removing_item_in_list.remove('hello')
print(removing_item_in_list) # the Output is ['hy', 'salam', 'wsalam']
print()
# If there are more than one item with the specified value, the remove() method removes the first occurrence

removing_occurence_of_item_in_list = ['corolla','grande','corolla','civic','grande','civic']
removing_occurence_of_item_in_list.remove('civic')
print(removing_occurence_of_item_in_list) # the output is ['corolla', 'grande', 'corolla', 'grande', 'civic']
print()

# Removed Specified Index
# to remove specified index their is a pop() method

removing_specified_index_of_list = ['red','green','blue','yello']
removing_specified_index_of_list.pop(1) # it will remove green
print(removing_specified_index_of_list) # the output is ['red', 'blue', 'yello']
print()

# if you do not specify the index the pop() automatically remove the last item
list_pop_method = [1,2,3,4,5,6,7,8,9,10]
list_pop_method.pop() # it will remove the last item from the list
print(list_pop_method) # the output is [1, 2, 3, 4, 5, 6, 7, 8, 9]
print()

# A del keyword is used to delete the list completely
del_list = [56,45,34,63,23,5,24]
del del_list
# print(del_list) # this will cause an error because you have succsesfully deleted del_list
print()


# Clear the list
# the clear() method is use to completely empty the list 
# the list still remains but 

clear_list = ['hello','to ','all ','the ','world']
clear_list.clear()
print(clear_list)