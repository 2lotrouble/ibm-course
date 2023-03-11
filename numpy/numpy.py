# import numpy library
import numpy as np

# Create a numpy array
a = np.array([0, 1, 2, 3, 4])
print(a)

# Print each element
print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])

print(np.__version__)

# Check the type of the array
print(type(a))

# Check the type of the values stored in numpy array
print(a.dtype)

# Get the size of numpy array
print(a.size)

# Get the number of dimensions of numpy array
print(a.ndim)

# Get the shape/size of numpy array
print(a.shape)
