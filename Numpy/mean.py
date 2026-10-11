import numpy as np
arr1=np.round(np.random.random((4,4))*100).astype('int32')
print(arr1)
mean_column=np.mean(arr1,axis=0)
print(mean_column)
mean_row=np.mean(arr1,axis=1)
print(mean_row)
