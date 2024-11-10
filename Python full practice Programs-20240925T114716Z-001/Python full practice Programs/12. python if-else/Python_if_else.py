# Python if else statementss
# Python Conditions and If statements
"""Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b"""
# These conditions can be used in several ways, most commonly in "if statements" and loops

# If
# An "if statement" is written by using the if keyword.
s = 34
b = 45
if s < b:
    print("b is greater than the s")
print()
# output
# b is greater than the s

# Identation:
# after the logical statement their become a identation 

# Elif
# The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

c = 34
x = 34
if c > x:
    print("c is greater than x")
elif c == x:
    print("c and x are equal")
print()
# output
# c and x are equal

# Else
# The else keyword catches anything which isn't caught by the preceding conditions.

m = 455
n = 342
if m < n:
    print("m is less than n")
elif m == n:
    print("m is equal to n")
else:
    print("m is greater than n")
print()
# output
# m is greater than n

# And
# The and keyword is a logical operator, and is used to combine conditional statements:
a1 = 344
b1 = 455
c1 = 123
if b1 > a1 and a1 > c1:
    print("yes b1 is greater than a1 and a1 is greater than c1")
# output
# yes b1 is greater than a1 and a1 is greater than c1

# Or
# The or keyword is a logical operator, and is used to combine conditional statements:

if a1 > b1 or c1 < b1:
    print("At least one conditon is true")
print()
# output
# At least one condition is True

#Not 
# The not keyword is a logical operator, and is used to reverse the result of the conditional statement:

if not a1 >b1:
    print("a1 is not greater than b1")
print()
# output
# a1 is not greater than b1

# Nested If
# ou can have if statements inside if statements, this is called nested if statements.

b2 = 56
if b2 > 10:
    print("above 10")
    if b2 > 20:
        print("above 20")
    if b2 > 30:
        print("above 30")
    else:
        print("but not above 40")
print()
# output
# above 10
# above 20
# above 30

# The pass Statement
# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error
a2 = 43
if a2 > 33:
    pass # this is for avoid a getting a error 

Enter_marks = int(input("Enter the number"))
if Enter_marks >=90:
    print("You got A+")
elif Enter_marks >=80:
    print("You got B+")
elif Enter_marks >=70:
    print("You got C+")
else:
    print("You are fail")





