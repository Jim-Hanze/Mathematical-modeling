import pandas as pd

# Load the data
data_2_1 = pd.read_excel("data/数据2.1 .xlsx")

# Display the first few rows of the dataset to understand its structure
data_2_1.head()

# Rename columns for better understanding
column_names = [
    "Final_Score", "Rank", "Award", "Second_Review_Range", "Reconsidered_Range",
    "Expert1_ID", "Expert1_Original_Score", "Expert1_Standard_Score", 
    "Expert2_ID", "Expert2_Original_Score", "Expert2_Standard_Score",
    "Expert3_ID", "Expert3_Original_Score", "Expert3_Standard_Score",
    "Expert4_ID", "Expert4_Original_Score", "Expert4_Standard_Score",
    "Expert5_ID", "Expert5_Original_Score", "Expert5_Standard_Score",
    "Second_Expert1_ID", "Second_Expert1_Original_Score", "Second_Expert1_Standard_Score", "Second_Expert1_Reconsidered_Score",
    "Second_Expert2_ID", "Second_Expert2_Original_Score", "Second_Expert2_Standard_Score", "Second_Expert2_Reconsidered_Score",
    "Second_Expert3_ID", "Second_Expert3_Original_Score", "Second_Expert3_Standard_Score", "Second_Expert3_Reconsidered_Score",
    "Dummy1", "Dummy2", "Dummy3"
]

data_2_1.columns = column_names
data_2_1 = data_2_1.iloc[2:].reset_index(drop=True)  # Drop the first two rows as they are redundant

# Display the cleaned data
data_2_1.head()
#data2_1_cleaned = data_2_1  ##自己后加

# 方案1: 直接平均法

# 计算每份作品的原始得分的平均值
data_2_1['Average_OriginalScore'] = data_2_1[
    ['Expert1_Original_Score', 'Expert2_Original_Score', 'Expert3_Original_Score', 'Expert4_Original_Score', 'Expert5_Original_Score']
].mean(axis=1)

# 方案2: 标准分法

# 计算每份作品的标准分的平均值
data_2_1['Average_StandardScore'] = data_2_1[
    ['Expert1_Standard_Score', 'Expert2_Standard_Score', 'Expert3_Standard_Score', 'Expert4_Standard_Score', 'Expert5_Standard_Score']
].mean(axis=1)

# Display the scores calculated using both methods for the first few entries
data_2_1[['Average_OriginalScore', 'Average_StandardScore']].head()

# Displaying the sorted works for both methods using the correct column name "最终成绩"
data_2_1[['Final_Score', 'Average_OriginalScore']].head(), data_2_1[['Final_Score', 'Average_StandardScore']].head()




import matplotlib.pyplot as plt

# Plotting the distribution of scores for both methods
plt.figure(figsize=(15, 6))

# Direct Average Method
plt.subplot(1, 2, 1)
plt.hist(data_2_1['Average_OriginalScore'], bins=50, color='skyblue', edgecolor='black')
plt.title('Distribution of Scores (Direct Average Method)')
plt.xlabel('Average Original Score')
plt.ylabel('Number of Works')

# Standard Score Method
plt.subplot(1, 2, 2)
plt.hist(data_2_1['Average_StandardScore'], bins=50, color='salmon', edgecolor='black')
plt.title('Distribution of Scores (Standard Score Method)')
plt.xlabel('Average Standard Score')
plt.ylabel('Number of Works')

plt.tight_layout()
plt.show()