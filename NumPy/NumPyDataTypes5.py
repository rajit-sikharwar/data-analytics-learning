import numpy as np

print("\n========== NUMPY DATA TYPES ==========\n")

# 1. Integer (i)
arr_int = np.array([1, 2, 3, 4, 5], dtype='i')
print("1. Integer (i)")
print("Array :", arr_int)
print("Dtype :", arr_int.dtype)
print("-------------------------------------")


# 2. Default Boolean
arr_bool_default = np.array([True, False, True])
print("2. Default Boolean")
print("Array :", arr_bool_default)
print("Dtype :", arr_bool_default.dtype)
print("-------------------------------------")


# 3. Boolean using 'b' (int8)
arr_bool_int = np.array([True, False, True], dtype='b')
print("3. Boolean using 'b' (int8)")
print("Array :", arr_bool_int)
print("Dtype :", arr_bool_int.dtype)
print("-------------------------------------")


# 4. Actual Boolean (?)
arr_bool = np.array([True, False, True], dtype='?')
print("4. Actual Boolean (?)")
print("Array :", arr_bool)
print("Dtype :", arr_bool.dtype)
print("-------------------------------------")


# 5. Unsigned Integer (u)
arr_uint = np.array([1, 2, 255], dtype='u1')
print("5. Unsigned Integer (u)")
print("Array :", arr_uint)
print("Dtype :", arr_uint.dtype)
print("-------------------------------------")


# 6. Float (f)
arr_float = np.array([1.5, 2.7, 3.9], dtype='f')
print("6. Float (f)")
print("Array :", arr_float)
print("Dtype :", arr_float.dtype)
print("-------------------------------------")


# 7. Complex (c)
arr_complex = np.array([1+2j, 3+4j], dtype='c')
print("7. Complex (c)")
print("Array :", arr_complex)
print("Dtype :", arr_complex.dtype)
print("-------------------------------------")


# 8. Timedelta (m)
arr_timedelta = np.array([5, 10, 15], dtype='m8[D]')
print("8. Timedelta (m)")
print("Array :", arr_timedelta)
print("Dtype :", arr_timedelta.dtype)
print("-------------------------------------")


# 9. Datetime (M)
arr_datetime = np.array(['2024-01-01', '2025-05-10'], dtype='M8[D]')
print("9. Datetime (M)")
print("Array :", arr_datetime)
print("Dtype :", arr_datetime.dtype)
print("-------------------------------------")


# 10. Object (O)
arr_object = np.array([1, 'hello', 3.5], dtype='O')
print("10. Object (O)")
print("Array :", arr_object)
print("Dtype :", arr_object.dtype)
print("-------------------------------------")


# 11. String (S - bytes)
arr_string = np.array(['apple', 'banana'], dtype='S')
print("11. String (S - bytes)")
print("Array :", arr_string)
print("Dtype :", arr_string.dtype)
print("-------------------------------------")


# 12. Unicode (U)
arr_unicode = np.array(['apple', 'banana'], dtype='U')
print("12. Unicode (U)")
print("Array :", arr_unicode)
print("Dtype :", arr_unicode.dtype)
print("-------------------------------------")


# 13. Void (V)
arr_void = np.array([b'abcd', b'efgh'], dtype='V4')
print("13. Void (V)")
print("Array :", arr_void)
print("Dtype :", arr_void.dtype)
print("-------------------------------------")


#Converting Data Type on Existing Arrays
arr = np.array([1.1, 2.1, 3.1, 4.1, 5.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)


print("\n========== NUMPY DATA TYPE CONVERSIONS ==========\n")
#Base Array (Integer)
arr_int = np.array([1, 0, 2, 0, 1, 3, 2, 1, 0])
print("Original Integer:", arr_int, arr_int.dtype)
print("-------------------------------------")

#1. Integer to Float
arr_float = arr_int.astype('f')
print("Int to Float:", arr_float, arr_float.dtype)