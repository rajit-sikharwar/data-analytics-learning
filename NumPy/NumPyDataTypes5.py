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

# 3. Actual Boolean (?)
arr_bool = np.array([True, False, True], dtype='?')
print("Actual Boolean:", arr_bool, arr_bool.dtype)

# 4. Unsigned Integer (u)
arr_uint = np.array([1, 2, 255], dtype='u1')
print("Unsigned Integer:", arr_uint, arr_uint.dtype)

# 5. Float (f)
arr_float = np.array([1.5, 2.7, 3.9], dtype='f')
print("Float:", arr_float, arr_float.dtype)

# 6. Complex Float (c)
arr_complex = np.array([1+2j, 3+4j], dtype='c')
print("Complex:", arr_complex, arr_complex.dtype)

# 7. Timedelta (m)
arr_timedelta = np.array([5, 10, 15], dtype='m8[D]')
print("Timedelta:", arr_timedelta, arr_timedelta.dtype)