from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Iris dataset
iris = load_iris()

# Create DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target

# Bar Chart
plt.figure(figsize=(8,5))
df.mean()[:-1].plot(kind='bar')
plt.title("Average Feature Values")
plt.ylabel("Average Value")
plt.show()

# Histogram
plt.figure(figsize=(8,5))
plt.hist(df['sepal length (cm)'], bins=10)
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Frequency")
plt.show()

# Scatter Plot
plt.figure(figsize=(8,5))
plt.scatter(df['sepal length (cm)'], df['petal length (cm)'])
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.title("Sepal Length vs Petal Length")
plt.show()

# Box Plot
plt.figure(figsize=(8,5))
sns.boxplot(data=df.iloc[:,0:4])
plt.title("Feature Distribution")
plt.show()

# Heatmap
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()