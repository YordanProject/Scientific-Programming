# Merubah tipe data ke tipe lain

# Integer
data_int = 10
print("Data = ", data_int, ", Tipe : ", type(data_int))

data_float = float(data_int)
data_bool = bool(data_int) # Akan false jika integer 0
data_str = str(data_int) 
print("Data berubah = ", data_float, ", Tipe : ", type(data_float))
print("Data berubah = ", data_bool, ", Tipe : ", type(data_bool))
print("Data berubah = ", data_str, ", Tipe : ", type(data_str))

# Float
data_float = 1.1
print("Data = ", data_float, ", Tipe : ", type(data_float))

data_int = int(data_float)
data_bool = bool(data_float) # Akan false jika integer 0
data_str = str(data_float) 
print("Data berubah = ", data_float, ", Tipe : ", type(data_float))
print("Data berubah = ", data_bool, ", Tipe : ", type(data_bool))
print("Data berubah = ", data_str, ", Tipe : ", type(data_str))
