# Python Add List Items

# Append Items
# To add item to the end of the list you can use the append() methods
appending_list = ['cow','sheeps','goats','hens']
appending_list.append('camels')
print(appending_list) # The output is ['cow', 'sheeps', 'goats', 'hens', 'camels']
print()


# Extend List
# To append elements from another list to the current list, use the extend() method.
extending_list1 = ['honda','bmw','changan','mercedes','Hyundai']
extending_list2 = ['civic','series 2','oshan x7','cla 200','sonata']
extending_list1.extend(extending_list2)  
print(extending_list1) # output ['honda', 'bmw', 'changan', 'mercedes', 'Hyundai', 'civic', 'series 2', 'oshan x7', 'cla 200', 'sonata']
print(extending_list2)# output ['civic','series 2','oshan x7','cla 200','sonata']
print()
# Note the elements will be added at the end of the string


# Add any iterable
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
this_is_list = ['apple','pineapple','bananas','citrus']
this_is_tuple = ('peach','manoges')
this_is_list.extend(this_is_tuple)
print(this_is_list) # output ['apple', 'pineapple', 'bananas', 'citrus', 'peach', 'manoges']