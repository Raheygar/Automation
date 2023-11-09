import numpy as np
#Initialize an array.(one-dimensional) 
a = np.array([1,2,3],dtype=object)  ##Pass a list within the brackets to initaliza array.
print(a)
#Initializa a two-dimensional array
##To do it you'will have a list within a list
b = np.array([[9,0,8,0,7,0],[1,2,3,4,5]],dtype=object)
print(b)
#Hot to get the dimension of your arrays
print(a.ndim)
print(b.ndim)

#Get shape. The shape function tells you the size row wise and column wise
print(a.shape)
print(b.shape)

#get type
print(a.dtype)
#get size
print(a.itemsize)

#get total size
print(a.nbytes)

#Float Type array
c = np.array([[6.4,1.2,2.5],[1.8,2.9,6.5,2.7]],dtype=object)
print(c.nbytes)