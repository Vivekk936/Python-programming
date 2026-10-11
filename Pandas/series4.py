import numpy as np 
import pandas as pd
k=pd.read_csv("youtube_2025_dataset_202504061614.csv")
print(k.head(5))
l=k['Total Subscribers']

print(l)
print(f"Total Sum of subscribers:{l.sum()}")
p=k['Total Videos']
print(f"Total Product of Total videos:{p.product()}")
print(f"Average of Total Videos:{p.mean()}")
print(f"Median of subscribers:{l.median()}")
print(f"Mode of subscribers:{l.mode()}")
print(f"Standard Devaition:",l.std())
print(f"Variance:",l.var())
print(f"Max:",l.max())
print(f"Min:",l.min())



