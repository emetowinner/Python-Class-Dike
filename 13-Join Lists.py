# How to join two list together using the + operator
list1 = ["a","b","c"]
list2 = [1,2,3]
list3 = list1 + list2
print(list3)

# How to join two lists using a for loop
for x in list2:
    list1.append(x)

print(list1)

# How to join two lists using the extend method
list3.extend(list2)
print(list3)