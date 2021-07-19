mydict = {
    "brand":"Ford",
    "model":"Mustang",
    "year":2021
}

# How to copy a dictionary using the copy method
second_dict = mydict.copy()
print(second_dict)

# How to copy a dictionary using the dict constructor

third_dict = dict(mydict)
print(third_dict)
