# Copy Lists
# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

# There are ways to make a copy, one way is to use the built-in List method copy()

this_is_list = ['shayan','komal','sajjad','kaneezfatima']
copying_this_is_list  = this_is_list.copy()
print(copying_this_is_list) # output ['shayan', 'komal', 'sajjad', 'kaneezfatima']
print(this_is_list) # output ['shayan', 'komal', 'sajjad', 'kaneezfatima']
print()

# another way to copy the list is list()
# using the list() method we also copy the list
hello_list = [1,2,3,4,5,6,7,7]
copying_hello_list = list(hello_list)
print(hello_list) # output [1, 2, 3, 4, 5, 6, 7, 7]
print(copying_hello_list) # output [1, 2, 3, 4, 5, 6, 7, 7]
print()