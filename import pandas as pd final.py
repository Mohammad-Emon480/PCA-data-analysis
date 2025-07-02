import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt


# Load data from Excel
excel_file =  (r"C:\PCA data analysis\PCA_Data1.xlsx") # Replace with your file path
df = pd.read_excel(excel_file)

# Extract numerical data and standardize
numerical_data = df.select_dtypes(include=[np.number])
scaler = StandardScaler()
scaled_data = scaler.fit_transform(numerical_data)

# Perform PCA
pca = PCA(n_components=2)  # Reduce to 2 principal components
principal_components = pca.fit_transform(scaled_data)

# Create results DataFrame
results_df = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])

# Plot explained variance
plt.figure(figsize=(8, 4))
plt.bar(range(1, 3), pca.explained_variance_ratio_, alpha=0.7)
plt.xlabel('Principal Components')
plt.ylabel('Explained Variance Ratio')
plt.title('Variance Explained by Principal Components')
plt.xticks([1, 2], ['PC1', 'PC2'])
plt.tight_layout()
plt.show()

