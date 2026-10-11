import pandas as pd

dataframe=pd.read_csv('youtube_2025_1.csv',index_col='Youtuber Name').squeeze('columns')
print(dataframe['Eric Patel'])
