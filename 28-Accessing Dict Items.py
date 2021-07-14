mydict = {
    "brand":"Ford",
    "model":"Mustang",
    "year":2021,
    "color":["red","white","blue"]
}

# How to access a dictionary item using the key
print(mydict["brand"])

# How to access a dictionary item using the get method
x = mydict.get("color")
print(x)

# How to get all the dictionary keys
x = mydict.keys()
print(x)

# How to get all the dictionary values
x = mydict.values()
print(x)

# How to get all the items in a dictionary
x = mydict.items()
print(x)