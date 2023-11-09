import numpy as np
a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)
#Output
# [[ 1  2  3  4  5  6  7]
#  [ 8  9 10 11 12 13 14]]

#get a specific element from 2-d array. Use indexing [row ,coloumn].We want 12
print(a[1,4])
#OUTPUT
# 12

#get a specific row
print(a[0,:])
#Output >> [1 2 3 4 5 6 7]

#get column
print(a[:,0])
#output [1 8]

#Basic indexing [start index,end index,step size]
#Get every other element in between 2 an 6 in the first row
print(a[0,1:6:2])
#OUTPUT>>> [2 4 6]

#Change a specific element in the n-d array
a[1,5] = 20
print(a)
#OUTPUT >> [[ 1  2  3  4  5  6  7]
#  [ 8  9 10 11 12 20 14]]

