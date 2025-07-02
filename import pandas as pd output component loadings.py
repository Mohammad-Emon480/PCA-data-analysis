import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt


# Load data from Excel
excel_file =  (r"C:\PCA data analysis\PCA_Data2.xlsx") # Replace with your file path
df = pd.read_excel(excel_file)

numerical_data = df.select_dtypes(include=[np.number])
# Remove 'Sl no' column if present
if 'Sl no' in numerical_data.columns:
    numerical_data = numerical_data.drop(columns=['Sl no'])
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

# Plot PCA projection
plt.figure(figsize=(8, 6))
plt.scatter(results_df['PC1'], results_df['PC2'], alpha=0.7)
plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.1f}%)')
plt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.1f}%)')
plt.title('PCA Projection of Dataset')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# Output component loadings
loadings = pd.DataFrame(
    pca.components_.T,
    columns=['PC1', 'PC2'],
    index=numerical_data.columns
)
print("Component Loadings:\n", loadings)
 # Replace with your file path
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

# Plot PCA projection
plt.figure(figsize=(8, 6))
plt.scatter(results_df['PC1'], results_df['PC2'], alpha=0.7)
plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.1f}%)')
plt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.1f}%)')
plt.title('PCA Projection of Dataset')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# Output component loadings
loadings = pd.DataFrame(
    pca.components_.T,
    columns=['PC1', 'PC2'],
    index=numerical_data.columns
)
print("Component Loadings:\n", loadings)
