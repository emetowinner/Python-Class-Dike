mydict = {
    "brand":"Ford",
    "model":"Mustang",
    "year":2021
}
print(mydict)

#Removing Dictionary Item using pop method
mydict.pop("year")

#Removing Dictionary item using popitem
mydict.popitem()

#Removing Dictionary item using the del keyword
del mydict["model"]

#Clear all items in a dictionary with clear method
mydict.clear()