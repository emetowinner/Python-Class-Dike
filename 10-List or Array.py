#List Type
x = ["apple","banana","cherry"]
print(x[0])# To access first element in the list
x[1] #To access second elemnet in the list
x[-1] #To access last element in the list

x = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
x[2:5] #Range indexing, collecting a range of values from a list
x[:5] #Collects from the begining to the specified number 
x[3:] #Collects from specified number to the end of the list

# Changing elements in a list
x[1] = "Carrot" #Changing single element in a list
x[1:3] = ["Banana","Watermelon"] #Changing multiple elements at the same time with different values
x[1:3] = ["Banana"]
x.insert(2,"Watermelon") # This inserts value at a specified index
x.append("Orange") # Used to add new value to the list

# Extend a list or add elements from another list to another list
y = ["Apple","Orange","Pea"]
x.extend(y)

#Remove an element from a list
x.remove("apple")

x.pop(2) # Removes element at the specified index

x.pop() # Removes the last element in the list

del x[0] # Removes element at the specified index

del x # Removes the list completely

x.clear() # Clears the elements in a list

# Looping through elements in a list
# We use for loop
x = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
for item in x:
    print(item)

counter  = 0
while counter < len(x):
    print(x[counter])
    counter += 1

# Looping through a list using list comprehension
y = [item for item in x]