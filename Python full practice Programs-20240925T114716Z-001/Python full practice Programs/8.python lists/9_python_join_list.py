# Joint List
#There are several ways to join, or concatenate, two or more lists in Python.

# One of the easiest ways are by using the + operator.

list1  =['a','b','c']
list2 = [1,2,3]
list3 = list1 + list2
print(list3) # output is ['a', 'b', 'c', 1, 2, 3]

# Another way to join two lists is by appending all the items from list2 into list1, one by one:
for i in list2:
    list1.append(i)
print(list1) # output ['a', 'b', 'c', 1, 2, 3]


# Or you can use the extend() method, where the purpose is to add elements from one list to another list:
list1.extend(list2)
print(list1)


