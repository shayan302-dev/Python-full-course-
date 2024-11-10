# Slicing
# you can return a range of characters by using the slice Syntax
# specify the start index and end index,seprated by colon, to return part of that string

# get the character from position 2 to 5(not included) it will print 2 to 4
x  = "hello shayan"
print(x[2:5]) # the output is llo 
print()
# h e l l o  s h a y a n
# 0 1 2 3 4 5 6 7 8 9 10 this is indexing 


# Slice From the Start

# By leaving out the start index, the range will start at the first character:
# Get the characters from the start to position 5 (not included):
print(x[:5])# its output is hello
print()
# it will default enter 0 in the blank space

# Slice to the end
# by leaving out the end index, the range wil got the end
print(x[2:]) # it output is llo shayan
print()


# Negative indexing
# use negative indexes to start the slice from the end of the string

# get the character 'o' in 'world!' (position -5)
# but not included 'd' in 'world!' (position -2)

a =  'Hello, World!'
print(a[-5:-2]) # The output is orl
# it indexing start from -1
# H    e   l    l   o      W   o   r   l    d    !
# -12 -11 -10  -9  -8  -7 -6  -5   -4  -3  -2    -1
print(a[-6:-1]) # it output is World 
print(a[-6:]) # it ouput is World!