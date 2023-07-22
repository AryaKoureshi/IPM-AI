print("Hello World!") # print

x = 5
print(type(x))

def myfunc1(x, y):
    return x+y

a = 'hello'
aa = "     hello      "
b = aa.strip()

Ua = b.upper()
aa = b.replace("he", "wtf")


for i in range(10):
    if i==2:
        print(i)
        break

c = {"a": 1, "b": 2}

import numpy as np
arr1 = np.array([[1, 2, 3], [4, 5, 6]])


# Create the original array
original_array = np.array([1, 2, 3, 4, 5])

# Create a view (slice) of the original array
view_array = original_array[1:4]

# Print both arrays
print("Original array:", original_array)
print("View array:", view_array)

# Modify the view array
view_array[0] = 10
view_array[1] = 20

# Print both arrays again
print("\nAfter modifying view array:")
print("Original array:", original_array)
print("View array:", view_array)

sub_arrays = np.where(original_array == 1)
original_array = np.sort(original_array)
from numpy import random
random.randint(100, size=5)

