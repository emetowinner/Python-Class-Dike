import numpy as np
# List of data types we have in numpy
"""
Below is a list of all data types in NumPy and the characters used to represent them.

i - integer
b - boolean
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )

"""
# 2-D array
arr = np.array([1,2,3,4,5,6,7],dtype="i")
print(arr.dtype)
print(arr)

# arr = np.array([[1,2,3,4],[2,3,4,5],[4,5,6,5],[8,5,4,3]])
# print(arr[1,1:3])