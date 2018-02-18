import numpy as np
from sklearn.decomposition import PCA
import pandas as pd

energy_data = './data/recs2009_public.csv'
df = pd.read_csv(energy_data, low_memory=False)
processed = [pd.to_numeric(df['DOEID'], errors="coerce").notnull()]
array = processed
print(array)
pca = PCA()
pca.fit(array)
print(pca.explained_variance_ratio_)
