# Python - Remove Dictionary Items
# There are several methods to remove items from a dictionary:

# pop()
removing_items_with_key =  {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964}
removing_items_with_key.pop('model') 
print(removing_items_with_key) # output {'brand': 'Ford', 'year': 1964}
print()


# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
removing_items_with_key.popitem()
print(removing_items_with_key) # output {'brand': 'Ford'}
print()
# del keyword
del removing_items_with_key['brand']
print(removing_items_with_key) #ouput {} empty dicitonary
print()

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# del thisdict
# print(thisdict) #this will cause an error because "thisdict" no longer exists.

# There is a del keyword also that delete the whole dicitonary keys and values and the dictionary also and give the error ifwe print the dicitionary 

# Clear() mehods
# There is a clear method  also that remove all the key and values of the dicitonary but not delete the dictionary like del keyword
clearning_dicitonary = {"age":23,
                        "year": 2023}
clearning_dicitonary.clear()
print(clearning_dicitonary) # ouput {} empty dictionary 
print()