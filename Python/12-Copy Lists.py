# How to copy a list using the copy method
x = ["apple","pea", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
y = x.copy()
print(y)

# How to copy a list using the list constructor
z = list(y)
print(z)

# How to copy a range of elements in a list
c = list(x[0:5])
print(c)