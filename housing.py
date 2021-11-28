import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import numpy as np
df = pd.read_csv('Housing_Data.csv')
y = df[['lotsize']]
df['fullbase'] = df['fullbase'].map({'yes':1 , 'no':0})
df['gashw'] = df['gashw'].map({'yes':1 , 'no':0})
df['airco'] = df['airco'].map({'yes':1 , 'no':0})
df['prefarea'] = df['prefarea'].map({'yes':1 , 'no':0})
x =  df[['price','bedrooms','bathrms','stories','garagepl','fullbase','airco','prefarea']]
x['driveway1'] = df['driveway'].map({'yes':1 , 'no':0})
x['recroom1'] = df['recroom'].map({'yes':1 , 'no':0})
x['price']=x['price']/x['price'].max()


#for linear model
from sklearn import linear_model
lmodel = linear_model.LinearRegression()
lmodel.fit(x,y)
print('Slope',lmodel.coef_)
print('Intercept',lmodel.intercept_)
p = lmodel.predict(x)
from sklearn import metrics
print('MAE',metrics.mean_absolute_error(y,p))




#Polynomial Model - use polynomial features
from sklearn.preprocessing import PolynomialFeatures
pol = PolynomialFeatures(degree = 8)
x_pol = pol.fit_transform(x)
x_pol

from sklearn.linear_model import LinearRegression
lmodel_p = LinearRegression()
lmodel_p.fit(x_pol,y)
Ypp = lmodel_p.predict(x_pol)
print('MAE',metrics.mean_absolute_error(y,Ypp))

error=[]
for i in range(1,10):
  pol = PolynomialFeatures(degree=i)
  x_pol = pol.fit_transform(x)
  lmodel_p.fit(x_pol,y)
  Ypp = lmodel_p.predict(x_pol)
  print(i,np.abs(y-Ypp).mean())
  error.append(np.abs(y-Ypp).mean())
plt.plot(range(1,10),error)
plt.show()  



from sklearn.preprocessing import StandardScaler
scl = StandardScaler()
Xs = pd.DataFrame(scl.fit_transform(x))
from sklearn.preprocessing import PolynomialFeatures
pol = PolynomialFeatures(degree=15)
x_pol = pol.fit_transform(Xs)
from sklearn.linear_model import LinearRegression
lmodel_p = LinearRegression()
lmodel_p.fit(x_pol,y)
Ypp = lmodel_p.predict(x_pol)
print(np.abs(y-Ypp).mean())