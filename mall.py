import pandas as pd
df = pd.read_csv('Mall_Customers.csv')
df = df[['Annual Income (k$)','Spending Score (1-100)']]
df
from sklearn.cluster import KMeans
kmodel = KMeans(n_clusters=5)
kmodel.fit(df)
Yp = kmodel.predict(df)
df['label'] =Yp
Yp = pd.DataFrame(Yp)
Yp

import matplotlib.pyplot as plt

plt.scatter(df['Annual Income (k$)'],df['Spending Score (1-100)'],c=df['label'])
plt.show()
dfs = df[['Annual Income (k$)','Spending Score (1-100)']]

#Elbow rule or Knee rule
loss = []
for i in range(1,15):
  kmodel = KMeans(n_clusters=i)

  kmodel.fit(dfs)
  loss.append(kmodel.inertia_)
plt.plot(range(1,15),loss)
plt.show()