import numpy as np
print("\n========== NUMPY DATA TYPES ==========\n")

#1.Integer (i)
arr_int = np.array([1, 2, 3], dtype='i')
print("1. Integer (i)")
print("Array :", arr_int)
print("Dtype :", arr_int.dtype)
print("-------------------------------------")


#2.Boolean (?) - Correct Boolean
arr_bool = np.array([True, False, True], dtype='?')
print("2. Boolean (?) - Correct")
print("Array :", arr_bool)
print("Dtype :", arr_bool.dtype)
print("-------------------------------------")


#3.Boolean using 'b' (actually int8)
arr_bool_b = np.array([True, False, True], dtype='b')
print("3. Boolean using 'b' (int8)")
print("Array :", arr_bool_b)
print("Dtype :", arr_bool_b.dtype)
print("-------------------------------------")


#4.Unsigned Integer (u)
arr_uint = np.array([1, 2, 255], dtype='u1')
print("4. Unsigned Integer (u)")
print("Array :", arr_uint)
print("Dtype :", arr_uint.dtype)
print("-------------------------------------")


#5.Float (f)
arr_float = np.array([1.5, 2.7, 3.9], dtype='f')
print("5. Float (f)")
print("Array :", arr_float)
print("Dtype :", arr_float.dtype)
print("-------------------------------------")


#6.Complex (correct way)
arr_complex = np.array([1+2j, 3+4j], dtype='complex128')
print("6. Complex (complex128)")
print("Array :", arr_complex)
print("Dtype :", arr_complex.dtype)
print("-------------------------------------")


#7.Character using 'c' (NOT complex)
arr_char = np.array([1, 2, 3], dtype='c')
print("7. Character ('c' - NOT complex)")
print("Array :", arr_char)
print("Dtype :", arr_char.dtype)
print("-------------------------------------")


#8.Timedelta (m)
arr_timedelta = np.array([5, 10], dtype='m8[D]')
print("8. Timedelta (m)")
print("Array :", arr_timedelta)
print("Dtype :", arr_timedelta.dtype)
print("-------------------------------------")


#9.Datetime (M)
arr_datetime = np.array(['2024-01-01'], dtype='M8[D]')
print("9. Datetime (M)")
print("Array :", arr_datetime)
print("Dtype :", arr_datetime.dtype)
print("-------------------------------------")


#10.Object (O)
arr_object = np.array([1, 'hello', 3.5], dtype='O')
print("10. Object (O)")
print("Array :", arr_object)
print("Dtype :", arr_object.dtype)
print("-------------------------------------")


#11.String (S - bytes)
arr_string = np.array(['apple', 'banana'], dtype='S')
print("11. String (S - bytes)")
print("Array :", arr_string)
print("Dtype :", arr_string.dtype)
print("-------------------------------------")


#12.Unicode (U)
arr_unicode = np.array(['apple', 'banana'], dtype='U')
print("12. Unicode (U)")
print("Array :", arr_unicode)
print("Dtype :", arr_unicode.dtype)
print("-------------------------------------")


#13.Void (V)
arr_void = np.array([b'abcd', b'efgh'], dtype='V4')
print("13. Void (V)")
print("Array :", arr_void)
print("Dtype :", arr_void.dtype)
print("-------------------------------------")


print("\n========== NUMPY DATA TYPE CONVERSIONS ==========\n")

#1.Integer conversions
arr_int = np.array([1, 0, 3])
print("Integer:", arr_int, arr_int.dtype)

print("Integer to Float:", np.array(arr_int, dtype='f'))
print("Integer to Boolean:", np.array(arr_int, dtype='?'))
print("Integer to Complex:", np.array(arr_int, dtype='complex128'))
print("Integer to String:", np.array(arr_int, dtype='S'))
print("Integer to Unicode:", np.array(arr_int, dtype='U'))

print("-------------------------------------")

#2.Float conversions
arr_float = np.array([1.7, 2.9, 3.1])
print("Float:", arr_float, arr_float.dtype)

print("Float to Integer:", np.array(arr_float, dtype='i'))   #decimal removed
print("Float to Boolean:", np.array(arr_float, dtype='?'))
print("Float to Complex:", np.array(arr_float, dtype='complex128'))

print("-------------------------------------")

#3.Boolean conversions
arr_bool = np.array([True, False, True])
print("Boolean:", arr_bool, arr_bool.dtype)
print("Boolean to Integer:", np.array(arr_bool, dtype='i'))
print("Boolean to Float:", np.array(arr_bool, dtype='f'))
print("Boolean to Complex:", np.array(arr_bool, dtype='complex128'))

print("-------------------------------------")

#4.String conversions
arr_str = np.array(['1', '2', '3'])
print("String:", arr_str, arr_str.dtype)
print("String to Integer:", np.array(arr_str, dtype='i'))
print("String to Float:", np.array(arr_str, dtype='f'))
print("String to Complex:", np.array(arr_str, dtype='complex128'))

print("-------------------------------------")

#5.Complex conversions
arr_complex = np.array([1+2j, 3+4j])
print("Complex:", arr_complex, arr_complex.dtype)
print("Complex to Float:", np.array(arr_complex, dtype='f'))   #imaginary part removed
print("Complex to Integer:", np.array(arr_complex, dtype='i')) #more data loss

print("-------------------------------------")

#6.Datetime conversions
arr_date = np.array(['2024-01-01', '2025-01-01'], dtype='M8[D]')
print("Datetime:", arr_date, arr_date.dtype)
print("Datetime to Integer:", np.array(arr_date, dtype='i'))

print("-------------------------------------")