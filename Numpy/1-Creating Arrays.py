import numpy as np

# print(np.__version__)

# How to create Numpy array using the array function
arr = np.array([1,2,3,4,5,6,7])
print(arr)
print(type(arr))

# How to create a numpy array from a list
list_array = [3,4,5,6,77]
arr = np.array(list_array)
print(arr)

# How to create a numpy array from a tuple
tuple_array = (1,9,8,5,3)
arr = np.array(tuple_array)
print(arr)

# Dimensions of array in numpy

# 0-D array
arr = np.array(42)
print(arr)
print("==============================")

# 1-D array
arr = np.array([1,2,3,4,5,6])
print(arr,arr.ndim)
print("==============================")

# 2-D array
arr = np.array([[1,2,3,4],[2,3,4,5],[4,5,6,5]])
print(arr,arr.ndim)
print("==============================")

# 3-D array
arr = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(arr,arr.ndim)
print("==============================")