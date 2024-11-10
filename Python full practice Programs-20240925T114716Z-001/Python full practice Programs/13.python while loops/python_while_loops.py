# Python While loops
# python loops
# python has two loops
# 1 while loop
# 2 for loop

# While loop
# with the while loop we can execute a set of statements as long as condition is true
# printing i as long as i is less than 9
i = 0
while i < 9:
    i+=1
    print(i)
print()
    # The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.

# Note: remember to increment i, or else the loop will continue forever.

# i = 1
# while i < 5:
#     print("hello to all the world") this loop  run infinite


# Break statement
# with the break statement we can  stop the loop even the while condition is True
# exit the loop when a == 4
a = 1
while a < 7:
    print(a)
    if a == 4:
        break
    a+=1
print()


# Continue statement
# With the continue statement we can stop the current iteration, and continue with the next:
# Continue to the next iteration if i is 3:
b = 0
while b < 6:
  b += 1
  if b == 3:
    continue
  print(b)
print()


# Else statement
s = 1
while s > 6: # if we change the sign in to less than the loop will execute
   print(s)
   s+=1
else:
   print("s is greater than 6 so loop  condition false and does not run")
print()



