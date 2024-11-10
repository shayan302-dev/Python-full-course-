# Python Dictionary
# This is the syntax of the dictionary data types
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# Dictionary
# The dictionary are use to store the data like Key:value pairs
# A dictionary  is a collection which is ordered , changeable and don't allow duplicate values

# As a python 3.7 version the dictionary is ordered In python 3.6 the dicitoinary is unordered


# Dictionary are written  with the curly brackets and have a key value:
creating_dictionary = {"name":"unknown",
                       "age":14,
                       "qualification":"matriculation"} # the name,age,qualification are keys and unknow,14,matriculation are the values
print(creating_dictionary) # The output is {'name': 'unknown', 'age': 14, 'qualification': 'matriculation'}
print()


# Items:
#  Refers to the key-value pairs in a dictionary. When you iterate over a dictionary, each iteration yields a tuple containing a key and its corresponding value. For example, {"name": "John", "age": 30}.items() yields ("name", "John") and ("age", 30).

#Values: 
# These are the actual data or objects associated with the keys in a dictionary. For example, in {"name": "John", "age": 30}, "John" and 30 are the values associated with the keys "name" and "age

# Note except the dictionary the values and the items are  the same things

# Dictionary Items
# dictionary items are oredered and the don't allow duplicates
# dictionary items are represented in the key:value pairs and can be refered using the key name
print(creating_dictionary["qualification"]) #  The Output is matriculation

