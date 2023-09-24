import pandas as pd
import matplotlib.pyplot as plt

data1 = pd.read_excel("data/数据1.xlsx")
data1_head = data1.head()
data1_head

desc_data1 = data1[['原始成绩求和']].describe()
fig, axes = plt.subplots(1, 1, figsize=(18, 15))
data1['原始成绩求和'].dropna().hist(ax=axes, bins=25, color='green', alpha=0.7)
axes.set_title("Data 1: Sum origin score")

plt.tight_layout()
plt.show()
