import numpy as np
arr1=np.round(np.random.random((4,4))*100).astype('int32')
print(arr1)
std_column=np.std(arr1,axis=0)
print(std_column)
std_row=np.std(arr1,axis=1)
print(std_row)
