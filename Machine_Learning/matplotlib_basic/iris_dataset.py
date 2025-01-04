import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
iris_data = load_iris()
iris_df = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
print("First few rows of the Iris dataset:")
print(iris_df.head())
plt.scatter(iris_df['sepal length (cm)'], iris_df['sepal width (cm)'])
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.title('Sepal Length vs Sepal Width')
plt.show()