import numpy as np


#Horizontal split-->np.hsplit(array,number of parts you want your array to be spliited at)
#Vertical split-->np.vsplit(array,number of parts you want your array to be spliited at)

array1=np.arange(1,13).reshape(3,4)
print(array1)
print('='*80 )
array2=np.arange(13,25).reshape(3,4)
print(array2)
print('='*80 )
Horinotal_array=np.hstack((array1,array2))
print(Horinotal_array)
print('='*80 )
Vertical_array=np.vstack((array1,array2))
print(Vertical_array)
print('='*80 )
print(np.hsplit(Vertical_array,2))