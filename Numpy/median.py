import numpy as np
arr1=np.round(np.random.random((4,4))*100).astype('int32')
print(arr1)
median_column=np.median(arr1,axis=0)
print(median_column)
median_row=np.median(arr1,axis=1)
print(median_row)
