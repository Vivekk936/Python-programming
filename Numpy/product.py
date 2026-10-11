import numpy as np
arr=np.arange(1,17).reshape(4,4)
PROD=np.prod(arr)
print(PROD)

#max value around row and column

arr1=np.round(np.random.random((4,4))*100).astype('int32')
print(arr1)
prod_column=np.prod(arr1,axis=0)
print(prod_column)
prod_row=np.prod(arr1,axis=1)
print(prod_row)
