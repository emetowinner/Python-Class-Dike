# How to add item to a set
x = {"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"}

x.add("watermelon")
print(x)

# How to add items from a different set
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
print(thisset)

# We can update a set with list or tuple items using the update method
mylist = ["corn","pea"]

thisset.update(mylist)
print(thisset)