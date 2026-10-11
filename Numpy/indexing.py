import numpy as np
matrix_1=np.round(np.random.random((5,5))*100).astype('int32')
print(matrix_1)
print(matrix_1[4,3])#arr[x axis][y axis]

arr=np.arange(1,9).reshape(2,2,2)#arr[z axis][x axis][y axis]
print(arr)
print(arr[1,0,1])

