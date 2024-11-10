# Python - Loop Dictionaries

# Loop Through a Dictionary
# When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well
printing_all_key_names_loop = {"shayan": 'respectable personality',
                               "rizwan":'angle of jannah'}
for i in printing_all_key_names_loop:
    print(i)
# output is 
# shayan
# rizwan
print()

# You can use the keys() method to return the keys of a dictionary
for x in printing_all_key_names_loop.keys():
    print(x)
# output is 
# shayan
# rizwan
print()

# You can use the items() method to return the items of the dictionary
for y , s in printing_all_key_names_loop.items():
    print(y,s)
# output is
# shayan respectable personality
# rizwan angle of jannah        
print()