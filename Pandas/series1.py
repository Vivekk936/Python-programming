import pandas as pd
import numpy as np
#Series from list
list=['India','China','Thailand','USA','Saudi Arabia']
print(pd.Series(list))

subject_names=['Math','Physics','Chemistry','Biology','English']
subject_marks=[90,92,96,85,70]
k=pd.Series(data=subject_marks,index=subject_names,name="Subject Marks Data",dtype='int32')
print(k)

values=np.arange(10,21)
print(pd.Series(values,dtype="int32"))

