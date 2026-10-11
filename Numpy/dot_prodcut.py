import numpy as np 
matrix_1=np.round(np.random.random((3,3))*100).astype('int32')

matrix_2=np.round(np.random.random((3,3))*100).astype('int32')
print(np.dot(matrix_1,matrix_2))