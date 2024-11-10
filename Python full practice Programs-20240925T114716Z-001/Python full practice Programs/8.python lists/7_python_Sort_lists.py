# Sort List Alphanumerically
# list objects have a sort mehthod that will sort the list alphanumarically , ascending by default
sorting_string_lists = ['banana','apple','citrus',]
sorting_string_lists.sort()
print(sorting_string_lists) # ouput ['apple', 'banana', 'citrus']
print()

# Sorting list numerically
sorting_numerically_list = [ 9,8,7,6,5,4,3,2,1]
sorting_numerically_list.sort()
print(sorting_numerically_list) # output [1, 2, 3, 4, 5, 6, 7, 8, 9]
print()

# Sorting descending order
# To sort descending, use the keyword argument reverse = True:
sorting_descending_string_lists =['apple','banana','citrus']
sorting_descending_string_lists.sort(reverse= True)
print(sorting_descending_string_lists) # output ['citrus', 'banana', 'apple']
print()
sorting_descending_numerically_lists = [1,2,3,4,5,6,7,8,9]
sorting_descending_numerically_lists.sort(reverse =  True)
print(sorting_descending_numerically_lists) # output [9, 8, 7, 6, 5, 4, 3, 2, 1]  

# Customizing the sort function
# You can also customize your own function by using the keyword argument key = function.
# The function will return a number that will be used to sort the list (the lowest number first)

# Sort the list based on how close the number is to 50:
def myfunction(n):
    return abs(n - 50)
this_is_list  = [67,90,100,50,55]
this_is_list.sort(key = myfunction)
print(this_is_list) # output is [50, 55, 67, 90, 100]        

