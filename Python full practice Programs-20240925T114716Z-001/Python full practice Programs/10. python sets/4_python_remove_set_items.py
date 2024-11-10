# Python Remove set Items
# To remove an item from the set you can use remove() and discard() methods 
removing_set_item = {'sindh',"balochistan","gilgit baltistan",'punjab',"kpk",'Azad Kashmir'}
removing_set_item.remove("gilgit baltistan")
removing_set_item.discard("Azad Kashmir")
print(removing_set_item) # it successfully delete the items from the sets
print()
# note discard() is only use on sets 
# note if the item does not exists the remove() raise an error but discard() can not raise an error

# There is a pop() method also but it remvoe  a random item form the set so you cannot be sure what item that gets removed.
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

# There is a del keyword also but it remove all the items in the set and the set also
delset = {'red',"green","blue"}
del delset
#print(delset) # This will raise an error becuase the del delete the items and the set itself so there is no set remain who have delset name

clearset = {'Pakistan',"india","iran"}
clearset.clear()
print(clearset) # its output is set() it will not delete the set but empty the set
print()
