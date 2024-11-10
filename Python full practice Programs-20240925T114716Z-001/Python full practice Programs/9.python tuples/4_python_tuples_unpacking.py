# Python Unpack tuples

# Unpacking a Tuple
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

# Packing a tuple:

fruits = ("apple", "banana", "cherry")

# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":

fruits = ("apple", "banana", "cherry",'shayan')
green, yellow, red, name = fruits  # extracting values back in to variables.

print(green)
print(yellow)
print(red)
print(name)
print()
# Note: The number of variables must match the number of values in the tuple, if not, you must use an asterisk to collect the remaining values as a list.

# Asterisk*
# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

cars = ('civic','corolla','yaris','changan oshan X7','crolla cross')
honda, toyota , *Changan = cars
print(honda)
print(toyota)
print(Changan) #output civic
                    #  corolla
                    #  ['yaris', 'changan oshan X7', 'crolla cross']
print()


# If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.

honda, *toyota, changan = cars
print(honda)
print(toyota)
print(changan) 
# output civic
# ['corolla', 'yaris', 'changan oshan X7']     
# crolla cross