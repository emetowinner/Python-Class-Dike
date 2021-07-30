import numpy as np

arr = np.array([1,2,3])

for x in arr:
    print(x)

# Looping through 2-D array elements
arr = np.array([[1,2,3,4],[2,3,4,5],[4,5,6,5],[8,5,4,3]])
for x in arr:
    print(x[1])

# Looping through 2-D array elements items
for x in arr:
    for item in x:
        pass
        print(item)

for y in np.nditer(arr):
    print(y)