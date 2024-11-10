# Dictionary Methods
# Python has a set of built-in methods that you can use on dictionaries.

"""1 clear()"""
# Removes all the elements from the dictionary

my_dict = {
    'name': 'John',
    'age': 25,
    'city': 'New York'
}
my_dict.clear()
print(my_dict) # output {}
print()


"""2 copy()"""
# return a copy of the dictionary

car_dict = {
    'Toyota': ['Corolla', 'Camry', 'Prius'],
    'Hyundai': ['Elantra', 'Sonata', 'Tucson'],
    'Honda': ['Civic', 'Accord', 'CR-V']
}
copying_car_dict = car_dict.copy() 
print(car_dict) # output {'Toyota': ['Corolla', 'Camry', 'Prius'], 'Hyundai': ['Elantra', 'Sonata', 'Tucson'], 'Honda': ['Civic', 'Accord', 'CR-V']}
print(copying_car_dict) # output {'Toyota': ['Corolla', 'Camry', 'Prius'], 'Hyundai': ['Elantra', 'Sonata', 'Tucson'], 'Honda': ['Civic', 'Accord', 'CR-V']}

# Another method is dict
using_dict_copying_car_dict = dict(car_dict)
print(using_dict_copying_car_dict) # output {'Toyota': ['Corolla', 'Camry', 'Prius'], 'Hyundai': ['Elantra', 'Sonata', 'Tucson'], 'Honda': ['Civic', 'Accord', 'CR-V']}
print()


"""3 fromkeys()"""
# fromkeys() method is used to create a new dictionary from a list of keys, all having the same specified value.

keys = ['Toyota',"Hyundai","Suzuki"]
dict_keys = dict.fromkeys(keys,'available')
print(dict_keys) # output {'Toyota': 'available', 'Hyundai': 'available', 'Suzuki': 'available'}
print()

# fromkeys() methods only assign one value to all the keys in the list 

"""4 get()"""
# The get() method in a dictionary is used to retrieve the value for a specified key. If the key is not found, it returns a default value (which is None if not specified).

student_grades = {
    'Alice': 85,
    'Bob': 76,
    'Charlie': 92,
    'David': 88
}
Bob_math_result = student_grades.get("Bob")
Charlie_math_result = student_grades.get("Charlie")
print('Bob numbers in math is ',Bob_math_result) # output  Bob numbers in math is 78
print("Charlie numbers in math is ",Charlie_math_result) # output Charlie numbers in mathi is 92
print(student_grades.get('Alice')) # output 85 
print()
# it take only one key as a argument which is called a key argument


"""5 items()"""
# Returns a list containing a tuple for each key value pair
for name,marks in student_grades.items():
    print(f"The name of Student is {name} and he got {marks} numbers from 100")
print()
# output
# The name of Student is Alice and he got 85 numbers from 100
# The name of Student is Bob and he got 76 numbers from 100
# The name of Student is Charlie and he got 92 numbers from 100
# The name of Student is David and he got 88 numbers from 100

"""6 keys()"""
# Returns a list containing the dictionary's keys
for takeingkeys in student_grades.keys():
    print(takeingkeys)
print()
# output
# Alice
# Bob
# Charlie
# David

"""7 pop()"""
# Removes the element with the specified key
car_details = {
    'brand': 'Toyota',
    'model': 'Camry',
    'year': 2022
}
car_details.pop("brand")
print(car_details) # output {'model': 'Camry', 'year': 2022}
print()
# it will delete the brand element from the car_details


"""8 popitem()"""
# Removes the last inserted key-value pair
car_details.popitem()
print(car_details) # output {'model': 'Camry'} brand could not print because we already delete it in the previous method
print()
# it will delete the last inserted element from the dictionary

"""9 setdefault()"""
# Define a dictionary
fruit_basket = {
    'apple': 3,
    'banana': 5,
    'orange': 2
}

# Using setdefault() to ensure 'grape' is in the dictionary with a default count of 0
fruit_basket.setdefault('grape', 0) # new key
fruit_basket.setdefault('orange', 34) # existing key
# in setdefault() the existing key value does not change 

# Print the updated dictionary
print("Updated Fruit Basket:")
print(fruit_basket) # output {'apple': 3, 'banana': 5, 'orange': 2, 'grape': 0}
print()


"""10 update()"""
# The update() method will update the dictionary with the items from the given argument.
person_info = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}
person_info.update({"name":"shayan"})
person_info.update({"car":"honda city"}) # it will also add the element in the dictionary
print(person_info) # output {'name': 'shayan', 'age': 30, 'city': 'New York','car':"honda city"}
print()


"""11 values()"""
# return a list of all values present in the dictionary
for a in person_info.values():
    print(a)
# output
# shayan
# 30
# New York
# honda cit