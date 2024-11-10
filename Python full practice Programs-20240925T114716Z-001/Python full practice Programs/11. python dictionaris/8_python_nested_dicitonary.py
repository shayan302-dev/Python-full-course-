cars  = {
    'Toyota':{"corolla grande":"80lac","yaris ativ":"55lac","Fortuner":"2crore"},
    "Honda":{'Civic':'83lac',"city":"48lac","honda vezel":"1.2crore"},
    "Suzuki":{'swift': "45lac","alto":"30lac","cultus":"42lac"}

}
print(cars) # output {'Toyota': {'corolla grande': '80lac', 'yaris ativ': '55lac', 'Fortuner': '2crore'}, 'Honda': {'Civic': '83lac', 'city': '48lac', 'honda vezel': '1.2crore'}, 'Suzuki': {'swift': '45lac', 'alto': '30lac', 'cultus': '42lac'}}
print()

# iterating dictionary
print(cars["Suzuki"]) # output {'swift': '45lac', 'alto': '30lac', 'cultus': '42lac'}
print()

# iteration dictionary value
print(cars["Suzuki"]['cultus']) # output is 42lac
print()

# iterating dictionary items using for loop
for i,s in cars.items():
    print(i,s)
print()

# output
# Toyota {'corolla grande': '80lac', 'yaris ativ': '55lac', 'Fortuner': '2crore'}
# Honda {'Civic': '83lac', 'city': '48lac', 'honda vezel': '1.2crore'}
# Suzuki {'swift': '45lac', 'alto': '30lac', 'cultus': '42lac'}


# changing the value of key in the nested dictionary
cars["Suzuki"]['cultus'] = '49lac'
print(cars["Suzuki"]["cultus"]) # output 49lac
print()

# removing item from the  nested dictionary
cars["Suzuki"].pop('cultus')
print(cars["Suzuki"]) # output {'swift': '45lac', 'alto': '30lac'}