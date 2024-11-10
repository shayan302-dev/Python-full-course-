# Python Classes and Objects
# Python is a object oriented programming
# Almost everything in python is an object
# A class is like a object  constructor , or a blueprint for creating a object

# Creating a Class
# to creat a class use the class keyword
 
class myClass:
    x = int(input("Enter the number: "))
    y = int(input("Enter the number: "))
    z = x + y 
    

# Create a object
# now we can use the class named myClass to create a object
p1 = myClass()
print(p1.z) 
print()

# The __init__() Function
# The example above  are classes and object in their simplest forms  and not really useful in real life applications
# To understand the meaning of classes we have to understand the built in __init__() function. All classses have a function called __init__() which is always executed when the class is initiated.
# use the  __init__() function to assign a value  to object properties, or other  operations that are necessary to do when the object is being created 

# Create a class named Person, use the __init__() function to assign values for name and age:
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        return(f"Hello my name is {self.name} and my age is {self.age}")

p2 = Person('Shayan',"18")
print(p2.name)
print(p2.age) 
print(p2.info())
# Note: The __init__() function is called automatically every time the class is being used to create a new object.
print()


# The __str__() Function
# The __str__() function controls what should be returned when the class object is represented as a string.

# If the __str__() function is not set, the string representation of the object is returned:


class Company:
    def __init__(self,name,share_price):
        self.name = name
        self.share_price = share_price
    def __str__(self):
        print(f'The name of company is {self.name} and the share price is {self.share_price}')
        return''
C1 = Company('ANWAR PHARMA',103)
print(C1)
print()


# Object Mehtods
# Objects can also contain methods. Methods in objects are function that belongs to the object.

# inserting a function in class that print shayan is a good boy
class Objects_Creation:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def func_print(self):
        print(self.name,'is a good boy')
O1 = Objects_Creation('Shayan',18)
O1.func_print() #Creating object method

# Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.



# The self Parameter
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class
class Parameters:
    def __init__(mymadobject,name):
        mymadobject.name = name
    def myfunc(abc):
        print('My name is',abc.name)
k2 = Parameters('Shayan')
k2.myfunc()
# Modifiying the object properties
k2.name = "Afzal"
k2.myfunc()
# Delete object properties
# del k2.name
# k2.myfunc() # give error because object have no attribute name well we delete it
# Delete object
# del k2 This will delete the object the above wala delete only property of object not object

# The Pass Statement
# If you make the class and leave it empty or want to make object in future you can simply write the pass 
class Pass:
    pass
# if we don't write the pass it wil give us error