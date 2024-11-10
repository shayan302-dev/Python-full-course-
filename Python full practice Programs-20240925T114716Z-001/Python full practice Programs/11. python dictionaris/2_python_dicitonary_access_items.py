# Python access Items

# Accessing Items
# You can access the item of dictionary by referring to its key name inside the square brackets
dictionary1 = {"Honda":"Civic",
               "Toyota" : "Corolla Grande",
               "Hyundai":"Sonata"}
print(dictionary1["Toyota"]) # output is Corolla Grande
# Here we enter the key in the square brackets

# get()
# There is a get() also that provide the same results
print(dictionary1.get('Toyota')) # output is Corolla Grande


# keys()
# There is a keys() mehtod that returns all the keys name present in the dictionary
print(dictionary1.keys()) # output is dict_keys(['Honda', 'Toyota', 'Hyundai'])
# The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.

# Example
# Add a new item to the original dictionary, and see that the keys list gets updated as well:
dictionary1["Suzuki"] = "Alto VXR"
# print(dictionary1.keys()) dict_keys(['Honda', 'Toyota', 'Hyundai', 'Suzuki'])
# The dict_keys is It's a way Python tells you that what follows are the keys of the dictionary.


# values()
# The values() method return all the values present in the dictionary
print(dictionary1.values()) # dict_values(['Civic', 'Corolla Grande', 'Sonata', 'Alto VXR'])
# The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.

# Example
# Make a change in the original dictionary, and see that the values list gets updated as well:
dictionary1['Changan'] = "Alsivin"
print(dictionary1.values()) # its output is dict_values(['Civic', 'Corolla Grande', 'Sonata', 'Alto VXR', 'Alsivin'])


# Get items
# The items() method will return each item in a dictionary, as tuples in a list.
print(dictionary1.items()) # its output is dict_items([('Honda', 'Civic'), ('Toyota', 'Corolla Grande'), ('Hyundai', 'Sonata'), ('Suzuki', 'Alto VXR'), ('Changan', 'Alsivin')])
 #  The returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list.
dictionary1["Kia"] = "Stonic"
print(dictionary1.items()) # its output is dict_items([('Honda', 'Civic'), ('Toyota', 'Corolla Grande'), ('Hyundai', 'Sonata'), ('Suzuki', 'Alto VXR'), ('Changan', 'Alsivin'), ('Kia', 'Stonic')])



# To check if key exists
# To check if key is exists in the dictionary use the keyword in 
# it can also be done like that 
# using the .keys() 

# if "Toyota" in dictionary1.keys():
if "Toyota" in dictionary1: # this only work for the keys not for the values for values use the other technique which is next
    print("yes the Toyota key is present in the dictionary1")



# To check if values exists in the dictonary 
if "Alsivin" in dictionary1.values():
    print('yes  the value is in the dictionary1')
