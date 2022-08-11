print('---------------------------------------------------------------------------------------')
#a part
import numpy
numbers = [1, 2.0, 3]
arr = numpy.array(numbers, dtype=str)
print(arr)
print("\n")

#b part
import numpy as np
array=np.array([[1,2,3,4],[5,6,8,9]],dtype = numpy.int32)
print(array)
print("\n")

#c part
numbers=numpy.array([[1,2,3,4],[5,6,7,8]],dtype = numpy.int32)
print(numbers.ndim)
print(numbers.shape)
print("\n")

#d part
num1 = numpy.random.randint(1, 100, 10)
print(num1)
print('---------------------------------------------------------------------------------------')
