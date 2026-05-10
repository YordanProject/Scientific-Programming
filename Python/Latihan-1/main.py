# Latihan Konversi satuan temperature
# Program konversi celcius ke satuan lain

print("===PROGRAM KONVERSI TEMPERATUR===\n")

celcius = float(input("Masukan suhu dalam celcius : "))
print("Masukan suhu dalam Celcius", celcius, "C")

print("===KONVERSI===\n")

# Reamur
'''
    R = (4/5)*C
'''
reamur = (4/5) * celcius
print("REAMUR = ", reamur, "R")

# Fahrenheit
'''
    F = ((9/5) * celcius) + 32 
'''
fahrenheit = ((9/5) * celcius) + 32
print("Fahrenheit = ", fahrenheit, "F")

# Kelvin
'''
    K = celcius + 273
'''
kelvin = celcius + 273
print("kelvin = ", kelvin, "K")


