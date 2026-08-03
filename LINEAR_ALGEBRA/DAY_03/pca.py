from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data
print("Original Shape:", X.shape)
pca = PCA(n_components=2)
X_new = pca.fit_transform(X)
print("Reduced Shape:", X_new.shape)
print("\nFirst 5 rows of transformed data:\n")
print(X_new[:5])