# Looping through elements in a tuple
# We use for loop
x = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
for item in x:
    print(item)

counter  = 0
while counter < len(x):
    print(x[counter])
    counter += 1