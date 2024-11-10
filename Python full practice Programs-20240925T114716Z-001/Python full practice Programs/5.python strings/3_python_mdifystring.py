# Python Modify Strings
# python has set of build in methods you can use on the strings

# Upper Case

# The upper() method give the string in the upper case

k = 'shayan' 
print(k.upper())# The output is SHAYAN
print()


# Lower Case
# the lower() method return the string in lower case
s = 'HOW Are you'
print(s.lower())# The output is how are you
print()


# Remove WhiteSpace
# The strip() method is use for removing the white space
a = '  Hello, world  '
print(a.strip()) # The output is Hello,World
print()
# note it will remove spaces from begginng and the end of the string


# Replace String
# The replace() method replace the string with other string
a = 'Donkey'
print(a.replace("D",'M')) # The output is Monkey
print()


# Split String
# The split() Method split the strings in to substrings if it finds instances of seprator
y = 'hello, shayan'
y1 = 'hello shayan'
print(y.split(',')) # the output is ['hello','shayan']
print(y1.split()) # The output is ['hello','shayan']


