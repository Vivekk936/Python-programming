import numpy as np
arr=np.arange(1,17).reshape(4,4)
SUM=np.sum(arr)
print(SUM)

#max value around row and column

arr1=np.round(np.random.random((4,4))*100).astype('int32')
print(arr1)
sum_column=np.sum(arr1,axis=0)
print(sum_column)
sum_row=np.sum(arr1,axis=1)
print(sum_row)
