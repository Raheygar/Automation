import numpy as np
##initializing an array "before"
before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)
print(before.shape)
##Output
#[[1 2 3 4]
#  [5 6 7 8]]
# (2, 4)  >>>shape of above array

##Lest say we want to change the shape of above array to (8,1)
print(before.reshape(8,1))
##Output
#[[1]
#  [2]
#  [3]
#  [4]
#  [5]
#  [6]
#  [7]
#  [8]]

##vertically stacking arrays. Stacking arrays one on top of other vertically
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
vertical = np.vstack((v1,v2,v2,v1,v1,v2))
print(vertical)

##output
# [[1 2 3 4]
#  [5 6 7 8]
#  [5 6 7 8]
#  [1 2 3 4]
#  [1 2 3 4]
#  [5 6 7 8]]

##Horizontally stacking up arrays.

horizontal = np.hstack((v1,v2))
print(horizontal)

##Output
# [1 2 3 4 5 6 7 8]