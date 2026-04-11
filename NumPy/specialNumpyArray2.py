import numpy as np

#Array filled with 0's
arr1 = np.zeros(4)
print(arr1)
print()
arr2 = np.zeros((4,3))
print(arr2)
print()

#Array filled with 1's
arr_one = np.ones(5)
print(arr_one)
print()
arr_one1 = np.ones((5,4)) #5-rows, 4-columns matrix with all values 1
print(arr_one1)
print()

#Create an Empty Array: empty array filled with elements that present in previous memory
arr_empty = np.empty(5)
print(arr_empty)
print()
arr_one1 = np.empty((5,4)) #5-rows, 4-columns matrix with all values 1
print(arr_empty)
print()

#elements within a range
arr_range = np.arange(5)
print(arr_range) #[0 1 2 3 4]
print()

#Array diagonal element filled with 1's
arr_diag = np.eye(3)
print(arr_diag)
print()
arr_diag1 = np.eye(5,5)
print(arr_diag1)