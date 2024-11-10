# Accessing the list items
# lists items are indexed so you can access them by refereing the index number
my_list = ['shayan','faisla','Subhan','fahad','Moneeb']
print(my_list[1]) #output faisla 
print()
# Note the list indexing start from 0

# There is also negative indexing in the lists
print(my_list[-1]) # output Subhan
print()
# Note negative indexing of lists start from 1 

#Range indexing 
# you can specify a range indexes by specifying where to start and where to end the range

# When specifying the list , the return value will be a new list with the specified items
print(my_list[2:5]) # The output is ['subhan','fahad','Moneeb']
print()
# Note: The search will start at index 2 (included) and end at index 5 (not included)
# remember the first item index is 0
print(my_list[:5]) # output ['shayan','faisla','Subhan','fahad','Moneeb']
print()
print(my_list[1:]) # output ['faisla','Subhan','fahad','Moneeb']
print()


# Range of negative indexing 
print(my_list[-4:-1]) # output ['faisla','subhan','fahad']
print()


# Check if Item Exists
# To determine if specified item is present in the the list or not
if 'shayan' in my_list:
    print('yes')

