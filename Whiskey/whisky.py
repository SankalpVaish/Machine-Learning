import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster.bicluster import SpectralCoclustering
whiskey=pd.read_csv("whiskies.txt")
whiskey["regions"]=pd.read_csv("regions.txt")
print(whiskey.head())
print(whiskey.tail())
print(whiskey.iloc[0:10])
print(whiskey.iloc[5:10, 0:5])
print(whiskey.columns)
flavours=whiskey.iloc[:, 2:14]
print(flavours)
corr_flavours=pd.DataFrame.corr(flavours.transpose())
print(corr_flavours)
plt.figure(figsize=(10,10))
plt.pcolor(corr_flavours)
plt.colorbar()
model=SpectralCoclustering(n_clusters=6, random_state=0)
model.fit(corr_flavours)
print(model.rows_)
print(np.sum(model.rows_, axis=1))
print(np.sum(model.rows_, axis=0))
print(model.row_labels_)