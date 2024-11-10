# Tuple Methods

 # python has two built in methods of the tuple that you can use on tuples


"""Method	Description
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found"""

# Count()
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5) 
print(x) # return 2 because there is a 5 two times in the tuple
print()

# Index()
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x) # return the index of the 8 which is 3
# indexing start from 0
print()
