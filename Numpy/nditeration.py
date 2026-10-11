import numpy as np 
arr=np.arange(1,9).reshape(2,2,2)#arr[z axis][x axis][y axis]
print(arr)
for i in np.nditer(arr): 
       print (i)
