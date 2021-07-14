# Ways to join two sets together

# Using the union method
set1 = {"a","b","c"}
set2 = {1,2,3}
set3 = set1.union(set2)
print(set3)

# Using the update method
set4 = {"a","b","c"}
set5 = {1,2,3}
set4.update(set5)
print(set4)

# Keeping only duplicate
set6 = {"a","b","c",1}
set7 = {1,2,"a",3}
set6.intersection_update(set7)
print(set6)

set8 = {"a","b","c",1}
set9 = {1,2,"a",3}
set10 = set8.intersection(set9)
print(set10)

# Keeping all, but not the duplicates
set11 = {"a","b","c",1}
set12 = {1,2,"a",3}
set11.symmetric_difference_update(set12)
print(set11)

set13 = {"a","b","c",1}
set14 = {1,2,"a",3}
set13 = set13.symmetric_difference(set14)
print(set13)