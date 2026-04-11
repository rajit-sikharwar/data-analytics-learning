import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)

#type check
print(type(arr))


#Use a tuple to create a NumPy array:
arr = np.array((1, 2, 3, 4, 5))
print(arr)


#---------------Dimensions in Arrays----------
#1. 0-D Array
arr = np.array(100)
print("\n0-D Array: \n", arr)

#2. 1-D Array
arr1d = np.array([1,2,3,4,5])
print("\n1-D Array: \n", arr1d)

#3. 2-D Array
arr2d = np.array([[1,2,3], [4,5,6]])
print("\n2-D Array: \n", arr2d)

#4. 3-D Array
arr3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print("\n3-D Array: \n", arr3d)
print(type(arr3d))