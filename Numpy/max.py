import numpy as np 
arr=np.arange(1,17).reshape(4,4)
MAX=np.max(arr)
print(MAX)

#max value around row and column

arr1=np.round(np.random.random((4,4))*100).astype('int32')
print(arr1)
max_column=np.max(arr1,axis=0)
print(max_column)
max_row=np.max(arr1,axis=1)
print(max_row)
