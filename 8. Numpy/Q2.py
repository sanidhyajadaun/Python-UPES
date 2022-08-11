print('---------------------------------------------------------------------------------------')

import numpy
import numpy as np

print(numpy.info(numpy.add))

print("\n")
a = np.array([52, 74, 7, 0, 0, 89])
print("Array is : ", end="")
print(a)
print("If all elements are non zero then True else false : ", end = "")
print(np.all(a))
print("\n")

b = np.array([45, 0, 26])
print("Array is : ", end="")
print(b)
print("If any element is non zero then true else false : ", end="")
print(np.any(b))
print("\n")

c = np.random.normal(1, 100, 15)
print("15 random numbers are : ", end="")
print(c)
print('---------------------------------------------------------------------------------------')

