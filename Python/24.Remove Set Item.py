# How to remove an item from a tuple
x = {"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"}

x.remove("apple")
print(x)

# How to remove an item in a set using the discard method
x.discard("banana")
print(x)

# We can use the pop method to remove an item fro a set
# NOTE You can't tell which item will get removed from the set
# It removes the item it finds at the last position of the set
x.pop() # This will remove a random item fro the set
print(x)

# We can use the clear method to clear the items in our set
x.clear()
print(x)

# We can delete a set using the python built-in del method
# del x
# print(x) # This will give you error