#  Python - add dictionary items
# Adding an item to the dictionary is done by using a new index key and assigning a value to it:

adding_value_in_dictionary = {"Toyota":'Corolla',
                              "honda":"civic",
                              "Suzuki":'alto'}
adding_value_in_dictionary["hyundai"] = "sonata"
print(adding_value_in_dictionary) # output {'Toyota': 'Corolla', 'honda': 'civic', 'Suzuki': 'alto', 'hyundai': 'sonata'}

# Update dictionary
# The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.
adding_value_in_dictionary.update({"Kia":"Sportage"})
print(adding_value_in_dictionary) # output {'Toyota': 'Corolla', 'honda': 'civic', 'Suzuki': 'alto', 'hyundai': 'sonata', 'Kia': 'Sportage'}

# The argument must be a dictionary, or an iterable object with key:value pairs.