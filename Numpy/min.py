import numpy as np
arr=np.arange(1,17).reshape(4,4)
MIN=np.min(arr)
print(MIN)

#max value around row and column

arr1=np.round(np.random.random((4,4))*100).astype('int32')
print(arr1)
min_column=np.min(arr1,axis=0)
print(min_column)
min_row=np.min(arr1,axis=1)
print(min_row)
