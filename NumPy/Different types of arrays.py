import numpy as np
##All 0 matrix
a = np.zeros((4,4))
print(a)
#OUTPUT 
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]

##ALL ones matrix
b = np.ones((3,6))
print(b)
#Output
# [[1. 1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1. 1.]]

##All any value. the value of the matrix should be mentioned in the end
c = np.full((5,5),25)
print(c)
#output

#Random decimal numbers
d = np.random.rand(4,2)
print(d)
# [[0.26160565 0.90179246]
#  [0.01790513 0.2969998 ]
#  [0.30864981 0.64500493]
#  [0.36907729 0.02426784]]

#The identity matrix is by nature a square matrix
e = np.identity(5)
print(e)
#Output
# [[1. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0.]
#  [0. 0. 1. 0. 0.]
#  [0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 1.]]

output = np.ones((5,5))
print(output)
new = np.zeros((3,3))
print(new)
new[1,1] = 9
print(new)
output[1:-1,1:-1] = new
print(output)

#output
#  [1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]]
# [[0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]]
# [[0. 0. 0.]
#  [0. 9. 0.]
#  [0. 0. 0.]]
# [[1. 1. 1. 1. 1.]
#  [1. 0. 0. 0. 1.]
#  [1. 0. 9. 0. 1.]
#  [1. 0. 0. 0. 1.]
#  [1. 1. 1. 1. 1.]]

##Becareful when copying arrays. Please use the copy() function always
a = np.array([1,2,3])
print(a)
b = a.copy()
print(b)
##output
# [1 2 3]
# [1 2 3]