import numpy as np
from sklearn.decomposition import PCA
import pandas as pd

energy_data = './data/recs2009_public.csv'
df = pd.read_csv(energy_data, low_memory=False)
array = df.values

cols = [c for c in df.columns if type(df[c][0]) is np.int64 or type(df[c][0]) is np.float64]
array = df[cols]

pca = PCA(n_components=15, svd_solver="full")
pca.fit(array)
print(pca.explained_variance_ratio_)
