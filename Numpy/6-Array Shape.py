import numpy as np

# 2-D array
arr = np.array([1,2,3,4,5,6,7],dtype="i")
x = arr.copy()
print(x.shape)

arr = np.array([[1,2,3,4,5],[2,3,4,5,5],[4,5,6,5,5],[8,5,4,3,5]])
print(arr.shape)

# How to shape an array
arr = np.array([1,2,3,4],ndmin=5)
print(arr,arr.shape)