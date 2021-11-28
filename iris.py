import pandas as pd
import matplotlib.pyplot as plt
iris=pd.read_csv('iris.csv')
#Independent variables or Features
X = iris[['SepalLengthCm' ,	'SepalWidthCm' ,	'PetalLengthCm' ,	'PetalWidthCm']]
#Dependent variables or Labels
Y = iris[['Species']]
Y = Y['Species'].map({'Iris-setosa':0, 'Iris-versicolor':1, 'Iris-virginica':2})
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest = train_test_split(X,Y,test_size=0.3,random_state=6)
from sklearn.neighbors import KNeighborsClassifier
kmodel = KNeighborsClassifier(n_neighbors=5)
#.fit() - used to train your model on existing data
kmodel.fit(xtrain,ytrain)
#testing accuracy
ypred_test = kmodel.predict(xtest)
print((ypred_test == ytest).sum() / len(ypred_test))
#.predict() - used to predict the o/p
q=kmodel.predict([[2.2,3.2,1.5,1.2]])

#k - no. of neighbors
#What will happen if no. of neighbors changes ?
#How to select best possible no. of neighbors ?
train_accuracy = []
test_accuracy = []
for i in range(1,15):
  km = KNeighborsClassifier(n_neighbors=i)
  km.fit(xtrain,ytrain)
  train_accuracy.append(km.score(xtrain,ytrain))
  test_accuracy.append(km.score(xtest,ytest))

plt.figure(figsize=(8,6))
plt.plot(range(1,15),train_accuracy)
plt.plot(range(1,15),test_accuracy)
plt.show()

import numpy as np
fname = np.array(['setosa','versicolor','virginica'])
fname[kmodel.predict([[6.1,8.2,1.5,2.7]])]


#sepel length, sepel width, petel length, petel width
x1 = iris['SepalLengthCm']
x2 = iris['SepalWidthCm']
x3 = iris['PetalLengthCm']
x4 = iris['PetalWidthCm']
Yc = Y.map({0:'r', 1:'g', 2:'b'})

#plt.scatter(x1,x2,c=Yc)
##plt.show()
#plt.scatter(x3,x4,c=Yc)
#plt.show()