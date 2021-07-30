# How to upadet an item in a tuple
y = ("apple","pea","banana","cherry")
print(y)
x = list(y)
x[0] = "carrot"
x[2] = "mango"
# x[1:3] = ["kiwi","mango"]
y = tuple(x)
print(y)

# The code below will give you errors
# y[0] = "orange"
# print(y)