# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load dataset
df = pd.read_csv("/content/heart Failure prediction Dataset.csv") 
# 1. Basic Info and Summary Statistics
print("Dataset Information:")
print(df.info())

print("\nDescriptive Statistics:")
print(df.describe())

# 2. Check for Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# 3. Distribution of Target Variable
sns.countplot(x='HeartDisease', data=df)
plt.title("Heart Disease Count (Target Variable)")
plt.show()

# 4. Histograms of Numeric Features
df.hist(figsize=(12, 10), bins=30)
plt.suptitle("Histograms of All Numeric Features")
plt.tight_layout()
plt.show()

# 5. Boxplots to Detect Outliers
plt.figure(figsize=(12, 6))
sns.boxplot(data=df[['Age', 'RestingBP', 'Cholesterol', 'MaxHR', 'Oldpeak']])
plt.title("Boxplots of Numeric Features")
plt.xticks(rotation=45)
plt.show()

# 6. Correlation Matrix
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='RdYlBu', fmt=".2f")
plt.title("Correlation Matrix")
plt.show()

# 7. Pairplot (useful to visualize relationships)
sns.pairplot(df[['Age', 'RestingBP', 'Cholesterol', 'MaxHR', 'HeartDisease']], hue='HeartDisease')
plt.suptitle("Pairplot of Key Features", y=1.02)
plt.show()

# 8. Categorical Feature Analysis
plt.figure(figsize=(12, 6))
sns.countplot(x='Sex', hue='HeartDisease', data=df)
plt.title("Heart Disease Count by Sex")
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(x='ChestPainType', hue='HeartDisease', data=df)
plt.title("Heart Disease Count by Chest Pain Type")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(12, 6))
sns.boxplot(x='HeartDisease', y='Oldpeak', data=df)
plt.title("Oldpeak vs Heart Disease")
plt.show()
