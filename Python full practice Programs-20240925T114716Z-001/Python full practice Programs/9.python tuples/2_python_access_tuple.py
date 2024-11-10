# Python Access Tuple
# ACCessing tuple items
tuple1 = ('helo',23,'turtule',453)
print(tuple1[1]) # output 23
print()

# negative indexing
print(tuple1[-2]) # output turtule
print()

# Range of indexing
print(tuple1[1:4]) # output (23,'turtule',453)
print() # the index 4 is not included


# Range of negative indexing
print(tuple1[-4:])# output ('helo',23,'turtule',453)
print()

# Check Item in list
if 'helo' in tuple1:
    print('yes it is in the tuple') #output yes it is in the tuple

