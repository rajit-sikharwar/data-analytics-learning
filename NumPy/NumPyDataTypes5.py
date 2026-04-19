import numpy as np
#integer
arr = np.array([1, 2, 3, 4, 5], dtype='i') #integer
print(arr)
print(arr.dtype)

#bool
arr = np.array([True, False, True]) 
print(arr)
print(arr.dtype)

#2. Boolean (b → actually int8)
arr_bool_int = np.array([True, False, True], dtype='b')
print("Boolean using 'b':", arr_bool_int, arr_bool_int.dtype)