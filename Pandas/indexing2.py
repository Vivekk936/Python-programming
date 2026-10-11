import pandas as pd
k=pd.read_csv("youtube_2025_dataset_202504061614.csv")
print(k.head(5))
l=k['Avg Video Length (min)']
print(l[::-1])