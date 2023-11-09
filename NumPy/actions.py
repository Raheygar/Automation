import numpy as np


##Loading data from a file:: This can be done using method genfromtxt() which takes in two
#arguments filename and delimiter.
filedata = np.genfromtxt('numbers.txt',delimiter=',')
print(filedata)

##Output

# [[  1.   2.   3.   4.   5.   6.   7.   8.   9.  10.  nan]
#  [ 11.  12.  13.  14.  15.  16.  17.  18.  19.  20.  nan]
#  [ 21.  22.  23.  24.  25.  26.  27.  28.  29.  30.  nan]
#  [ 31.  32.  33.  34.  35.  36.  37.  38.  39.  40.  nan]
#  [ 41.  42.  43.  44.  45.  46.  47.  48.  49.  50.  nan]
#  [ 51.  52.  53.  54.  55.  56.  57.  58.  59.  60.  nan]
#  [ 61.  62.  63.  64.  65.  66.  67.  68.  69.  70.  nan]
#  [ 71.  72.  73.  74.  75.  76.  77.  78.  79.  80.  nan]
#  [ 81.  82.  83.  84.  85.  86.  87.  88.  89.  90.  nan]
#  [ 91.  92.  93.  94.  95.  96.  97.  98.  99. 100.  nan]]


##Advanced Indexing. Fulfilling a certain condition and then print out in Boolean 
print(filedata>50)

##Output prints out the index positions where above condition is true or false.
# [[False False False False False False False False False False False]
#  [False False False False False False False False False False False]
#  [False False False False False False False False False False False]
#  [False False False False False False False False False False False]
#  [False False False False False False False False False False False]
#  [ True  True  True  True  True  True  True  True  True  True False]
#  [ True  True  True  True  True  True  True  True  True  True False]
#  [ True  True  True  True  True  True  True  True  True  True False]
#  [ True  True  True  True  True  True  True  True  True  True False]
#  [ True  True  True  True  True  True  True  True  True  True False]]

##Print out the values which fulfill a certain condition
print(filedata[filedata>50])

##output
# [ 51.  52.  53.  54.  55.  56.  57.  58.  59.  60.  61.  62.  63.  64.
#   65.  66.  67.  68.  69.  70.  71.  72.  73.  74.  75.  76.  77.  78.
#   79.  80.  81.  82.  83.  84.  85.  86.  87.  88.  89.  90.  91.  92.
#   93.  94.  95.  96.  97.  98.  99. 100.]

##Satisfying a condition singular
print(np.any(filedata>50,axis=0))

##Output
# [ True  True  True  True  True  True  True  True  True  True False]

##Satisfying multiple conditions
print(((filedata>50) & (filedata<100)))

##output
# [[False False False False False False False False False False False]
#  [False False False False False False False False False False False]
#  [False False False False False False False False False False False]
#  [False False False False False False False False False False False]
#  [False False False False False False False False False False False]
#  [ True  True  True  True  True  True  True  True  True  True False]
#  [ True  True  True  True  True  True  True  True  True  True False]
#  [ True  True  True  True  True  True  True  True  True  True False]
#  [ True  True  True  True  True  True  True  True  True  True False]
#  [ True  True  True  True  True  True  True  True  True False False]]
