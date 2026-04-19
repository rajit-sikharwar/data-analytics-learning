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

# 8. Datetime (M)
arr_datetime = np.array(['2024-01-01', '2025-05-10'], dtype='M8[D]')
print("Datetime:", arr_datetime, arr_datetime.dtype)

# 9. Object (O)
arr_object = np.array([1, 'hello', 3.5], dtype='O')
print("Object:", arr_object, arr_object.dtype)

# 10. String (S → bytes)
arr_string = np.array(['apple', 'banana'], dtype='S')
print("String (bytes):", arr_string, arr_string.dtype)

# 11. Unicode String (U)
arr_unicode = np.array(['apple', 'banana'], dtype='U')
print("Unicode:", arr_unicode, arr_unicode.dtype)

# 12. Void / Fixed Memory (V)
arr_void = np.array([b'abcd', b'efgh'], dtype='V4')
print("Void:", arr_void, arr_void.dtype)