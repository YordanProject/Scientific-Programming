# Operasi aritmatika

a = 10
b = 3

# Operasi Tambah +
hasil = a + b
print(a, "+", b, '=', hasil)

# Operasi Pengurangan -
hasil = a - b
print(a, "-", b, '=', hasil)

# Operasi Perkalian
hasil = a * b
print(a, "*", b, '=', hasil)

# Operasi bagi +
hasil = a / b
print(a, "/", b, '=', hasil)

# Eksponen/Pangkat **
hasil = a ** b
print(a, "**", b, '=', hasil)

# Modulus %
hasil = a & b
print(a, "%", b, '=', hasil)

# Floor Divison
hasil = a // b
print(a, "//", b, '=', hasil)

# Prioritas Operasi
'''
    1. ()
    2. Eksponen **
    3. Perkalian dan teman-teman * / % //
    4. Pertambahan dan pengurangan + -  
'''
x = 3
y = 2
z = 4

hasil = x + y * z // x % y ** z
print(x, '+', y, '*', z, '//', x, '%', y, '**', z, '=', hasil)

