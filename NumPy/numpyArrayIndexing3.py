import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr[0])
print(arr[2] + arr[3]) #sum of 3rd and 4th element

#Accessing 2D arrays
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', arr[0, 1])