import numpy as np

# Membuat Vector
a = np.array([1,2,3,4,5])
b = np.array([1.5, 2.5, 5, 6, 7])

# Membuat vector dengan range
c = np.arange(1,10,2)

# Membuat Linspace
d = np.linspace(1,10,4)

# Array Multidimensi/Matrix
e = np.array([(1,2,3), (4,5,6)])

# Matrix dengan nilai nol
f = np.zeros((5,5))

# Matrix dengan nilai satu
g = np.ones((6,5))

# Matrix Identitas
h1 = np.identity(5)
h2 = np.eye(5)

# Display
print(h2)