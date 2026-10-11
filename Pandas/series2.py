import numpy as np 
import pandas as pd
# Dictionary to Series
data_items={
    'Maths':90
    ,'English':85,
    'Bilogy':94,
    'Hindi':100
}
print(pd.Series(data_items))
#custom Index
values=[1,2,3,4,5]
k=pd.Series(data=values,index=['a','b','c','d','e'])
print(k)
