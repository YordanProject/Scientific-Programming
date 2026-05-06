import numpy as np

# List Python
a = [1,2,3,4,5]
b = [6,7,8,9,10]

# Array Numpy
anp = np.array([1,2,3,4,5])
bnp = np.array([6,7,8,9,10])

# Elemen Wise Operation
# Penjumlahan
hasil = anp+bnp

# Pengurangan
hasil = anp-bnp

# Perkalian
hasil = anp*bnp

# Pembagian
hasil = anp / bnp

# Kuadrat
hasil = anp ** bnp

# Multidimensi array numpy
c = np.array(([1,2,3], [4,5,6]))
d = np.array(([7,8,9], [-1,-2,-3]))

hasil = c + d
hasil = c * d
print(hasil)