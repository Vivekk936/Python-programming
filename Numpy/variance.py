import numpy as np
arr1=np.round(np.random.random((4,4))*100).astype('int32')
print(arr1)
var_column=np.var(arr1,axis=0)
print(var_column)
var_row=np.var(arr1,axis=1)
print(var_row)
