import pandas as pd

dataframe=pd.read_csv('youtube_2025_1.csv',index_col='Youtuber Name').squeeze('columns')
dataframe['Eric Patel']=70
print(dataframe)

dataframe['Vivek Singh']=9
print(dataframe.tail())

dataframe[2:10]=18
print(dataframe.head(20))

dataframe.iloc[[4,45,2000]]=[32,42,52] #we using iloc as our indexing is string "Youtuber name"
print(dataframe.iloc[[4,45,2000]]) 