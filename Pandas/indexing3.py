import pandas as pd
k=pd.read_csv("youtube_2025_dataset_202504061614.csv")
print(k.head(5))
l=k['Avg Video Length (min)']
print(l[[7,4,5]])#fancy indexing
print(l[[1008,1000,2999]])
 
