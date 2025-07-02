import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Load data from Excel
excel_file = (r"C:\PCA data analysis\PCA_Data2.xlsx")
df = pd.read_excel(excel_file)

# Extract numerical data and standardize
numerical_data = df.select_dtypes(include=[np.number])
scaler = StandardScaler()
scaled_data = scaler.fit_transform(numerical_data)

# Perform PCA
pca = PCA(n_components=5)  # Reduce to 2 principal components
principal_components = pca.fit_transform(scaled_data)

# Create results DataFrame
results_df = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2' , 'PC3', 'PC4', 'PC5'])


#
# 
#  Plot PCA projection
plt.figure(figsize=(8, 6))

plt.scatter(results_df['PC1'], results_df['PC2'], alpha=0.7)
plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.1f}%)')
plt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.1f}%)')
plt.title('PCA Projection of Dataset')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()




