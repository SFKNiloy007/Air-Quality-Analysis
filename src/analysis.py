import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('updated_pollution_dataset.csv')  
df.head()
df.info() 
df.describe()  
df.isnull().sum()

air_quality_counts = df['Air Quality'].value_counts()
air_quality_percentage = df['Air Quality'].value_counts(normalize=True) * 100

print(air_quality_counts)
print(air_quality_percentage)

numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
df[numeric_columns].describe()
df['Air Quality'].value_counts()

fig, axes = plt.subplots(2, 2, figsize=(16, 10))

air_quality_counts.plot(kind='bar', color='skyblue', ax=axes[0, 0])
axes[0, 0].set_title('Air Quality Counts')
axes[0, 0].set_ylabel('Count')
axes[0, 0].set_xlabel('Air Quality')

air_quality_counts.plot(kind='pie', autopct='%1.1f%%', ax=axes[0, 1])
axes[0, 1].set_title('Air Quality Percentage Distribution')
axes[0, 1].set_ylabel('')

numeric_df = df.select_dtypes(include=['float64', 'int64'])
corr_matrix = numeric_df.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=axes[1, 0])
axes[1, 0].set_title('Correlation Heatmap')

df['Temperature'].plot(kind='line', ax=axes[1, 1])
axes[1, 1].set_title('Temperature Over Time')
axes[1, 1].set_ylabel('Temperature')
axes[1, 1].set_xlabel('Index')

plt.tight_layout()
plt.show()
