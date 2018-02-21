import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
import matplotlib.pyplot as plt
import pandas as pd

energy_data = './data/recs2009_public.csv'
df = pd.read_csv(energy_data, low_memory=False)
cols = [
    c for c in df.columns if isinstance(
        df[c][0],
        np.int64) or isinstance(
            df[c][0],
        np.float64)]
cols = cols[1:]
array = df[cols]
stddev = np.std(df['KWH'])
plt.plot(df['KWH'])
plt.ylabel("Usage (KWH)")
plt.xlabel("household")
plt.show()
print("stddev")
print(stddev)

scaled = pd.DataFrame(scale(array), columns=cols)
pca = PCA(n_components=40, svd_solver="full")
new = pca.fit_transform(scaled)
var = pca.explained_variance_ratio_
var1 = np.cumsum(np.round(pca.explained_variance_ratio_, decimals=4) * 100)
features = np.where(new == new.max(axis=0))
for i in features[1]:
    print("'" + cols[i] + "',")
# print(pd.DataFrame(pca.components_,columns=scaled.columns))
plt.plot(var1)
plt.ylabel("variance")
plt.xlabel("component")
plt.show()
