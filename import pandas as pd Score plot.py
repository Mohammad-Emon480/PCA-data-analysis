import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Load data from Excel
excel_file = r"C:\PCA data analysis\PCA_Data1.xlsx"
df = pd.read_excel(excel_file)

numerical_data = df.select_dtypes(include=[np.number])


# Remove 'Sl no' column if present
if 'Sl no' in numerical_data.columns:
    numerical_data = numerical_data.drop(columns=['Sl no'])
scaler = StandardScaler()
scaled_data = scaler.fit_transform(numerical_data)


# Perform PCA
pca = PCA(n_components=5)  # Reduce to 2 principal components
principal_components = pca.fit_transform(scaled_data)

# Create results DataFrame
results_df = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2' , 'PC3', 'PC4', 'PC5'])



#  Biplot for PC1 and PC2

plt.figure(figsize=(10, 7))
ax = plt.gca()
ax.set_facecolor("#7D86A2")  # High contrast dark background
plt.rcParams['axes.edgecolor'] = 'white'
plt.rcParams['axes.labelcolor'] = 'white'
plt.rcParams['xtick.color'] = 'white'
plt.rcParams['ytick.color'] = 'white'
plt.rcParams['text.color'] = 'white'


# Scatter plot of the samples

plt.scatter(results_df['PC1'], results_df['PC2'], alpha=0.7, label='Samples', color='yellow')
# Draw vectors for each variable
for i, var in enumerate(numerical_data.columns):
    plt.arrow(0, 0, pca.components_[0, i]*max(results_df['PC1']), pca.components_[1, i]*max(results_df['PC2']),
              color='r', alpha=0.7, head_width=0.1)
    plt.text(pca.components_[0, i]*max(results_df['PC1'])*1.1, pca.components_[1, i]*max(results_df['PC2'])*1.1,
             var, color='r', ha='center', va='center')
plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.1f}%)')
plt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.1f}%)')
plt.title('PCA Biplot (PC1 vs PC2)')
plt.grid(alpha=0.3)
plt.tight_layout()
plt.legend()
plt.show()