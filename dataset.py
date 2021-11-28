import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import numpy as np
df = pd.read_csv('dataset.txt',header=None)
x=np.array(df[[0]])
y=np.array(df[[1]])
x_mean=x.mean()
y_mean=y.mean()
n=((x-x_mean)*(y-y_mean)).sum()
d=((x-x_mean)*(x-x_mean)).sum()
m=n/d
c=y_mean-m*x_mean
print(m,c)
yp=m*x+c
plt.scatter(x,y)
#plt.plot(x,yp,x='r')
plt.show()
#mean absolute error
print(np.abs(y - yp).mean())
#mean squared error
print(((y-yp)**2).mean())

from sklearn import linear_model
lmodel = linear_model.LinearRegression()

lmodel.fit(x,y)
print('Slope',lmodel.coef_)
print('Intercept',lmodel.intercept_)

p = lmodel.predict(x)

from sklearn import metrics
print('MAE',metrics.mean_absolute_error(y,p))
print('MSE',metrics.mean_squared_error(y,p))

from sklearn.preprocessing import PolynomialFeatures
pol = PolynomialFeatures(degree = 3)
x_pol = pol.fit_transform(x)
x_pol
#Polynomial Model - use polynomial features
from sklearn.linear_model import LinearRegression
lmodel_p = LinearRegression()
lmodel_p.fit(x_pol,y)
Ypp = lmodel_p.predict(x_pol)
plt.scatter(x,y)
plt.plot(x,Ypp,c='g')
plt.show()