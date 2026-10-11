import numpy as np

#Horizontal Stacking->Row by Row joining is done->hstack()
#Vertical Stacking->Column by COlumn joining is done->vstack()

array1=np.arange(1,13).reshape(3,4)
print(array1)
array2=np.arange(13,25).reshape(3,4)
print(array2)
Horinotal_array=np.hstack((array1,array2))
print(Horinotal_array)

Vertical_array=np.vstack((array1,array2))
print(Vertical_array)

