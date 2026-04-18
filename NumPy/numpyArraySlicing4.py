import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(arr[1:5]) #Slice elements from index 1 to index 5 from the

#Slice elements from index 5 to the end of the array:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(arr[5:])

#Slice elements from the beginning to index 5 (not included):
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(arr[:5])

#Negative Slicing: Use the minus operator to refer to an index from the end:
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1])