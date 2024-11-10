# Python - Change Dictionary Items
# Change values
# You can change the value of specific item by referring to its key name
changing_dictionary_item = {'year':2024,
                            "month" : "march",
                            "day": 11 }
changing_dictionary_item['year'] = 2006
print(changing_dictionary_item) # output {'year': 2006, 'month': 'march', 'day': 11}


# Update()
# The update() method will update the dictionary with the items from the given argument.
changing_dictionary_item.update({"month":"feburary"})
print(changing_dictionary_item) # output {'year': 2006, 'month': 'feburary', 'day': 11}

