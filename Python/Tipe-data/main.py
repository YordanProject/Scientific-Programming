# Integer, angka yang tidak ada komanya
data_integer = 1
print(type(data_integer))
print("- Data : ", data_integer,", Bertipe : ", type(data_integer))

# Float, angka berkoma
data_float = 1.5
print(type(data_float))
print("- Data : ", data_float,", Bertipe : ", type(data_float))

# String
data_string = "Bambang"
print(type(data_string))
print("- Data : ", data_string,", Bertipe : ", type(data_string))

# Boolean
data_bool = True
print(type(data_bool))
print("- Data : ", data_bool,", Bertipe : ", type(data_bool))

## Tipe data Khusus
# Bilangan kompleks
data_complex = complex(5,6)
print(type(data_complex))
print("- Data : ", data_complex,", Bertipe : ", type(data_complex))

# Tipe data dari bahasa C

from ctypes import c_double
data_c_double = c_double(10.5)
print(type(data_c_double))
print("- Data : ", data_c_double,", Bertipe : ", type(data_c_double))