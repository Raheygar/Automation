import numpy as np

##Element wise arithmetic 
a = np.array([1,2,3,4])
print(a)

##OUTPUT
# [1 2 3 4]

##Lets add 2 to each element of the array a
print(a+2)

##OUTPUT
# [3 4 5 6]

##Subtracting 1 from each element of the array a
print(a-2)

##OUTPUT
# [-1  0  1  2]

##Multiplying each element of the array a with 2
print(a*2)

##OUTPUT
# [2 4 6 8]

##dividing each element by 3 in the array
print(a/3)

##OUTPUT
# [0.33333333 0.66666667 1.         1.33333333]

##Adding two arrays. Lets initialize new array b and add it to a

b = np.array([5,6,7,8])
print(a+b)

#OUTPUT after adding the two arrays
# [ 6  8 10 12]

##POWER operation
print(a**2)

#OUTPUT
# [ 1  4  9 16]

##Sin and Cos of elemnets in the array a
print(np.sin(a))
#OUTPUT  >>>>   [ 0.84147098  0.90929743  0.14112001 -0.7568025 ]
print(np.cos(a))
#OUTPUT  >>>>>  [ 0.54030231 -0.41614684 -0.9899925  -0.65364362]


######Linear Algebra######

##Multiplying two matricies
c = np.ones((2,3))
print(c)
d = np.full((3,4),3)
print(d)
print(np.matmul(c,d))

##OUTPUT
# [[1. 1. 1.]
#  [1. 1. 1.]]
# [[3 3 3 3]
#  [3 3 3 3]
#  [3 3 3 3]]
# [[9. 9. 9. 9.]
#  [9. 9. 9. 9.]]


