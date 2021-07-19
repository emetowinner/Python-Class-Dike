# By default looping through a dictionary will give you the dictionary keys not values

# Looping through dictionary keys
mydict = {
    "brand":"Ford",
    "model":"Mustang",
    "year":2021
}

for x in mydict:
    print(x)

# Looping through to capture the values
for x in mydict:
    print(mydict[x])

# Looping through dictionary values
for x in mydict.values():
    print(x)

# Looping through dictionary keys
for x in mydict.keys():
    print(x)

# Looping through dictionary keys and values
for key,value in mydict.items():
    print(key,value)