import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import numpy as np
adv = pd.read_csv('Advertising.csv')
x = adv['TV']
y = adv['sales']

x_mean = x.mean()
y_mean = y.mean()

num = ((x - x_mean) * (y - y_mean)).sum()
den = ((x - x_mean) * (x - x_mean)).sum()
m = num/den
print(m)

c = y_mean - m*x_mean
print(c)

yp = m*x + c

plt.scatter(x,y)
plt.plot(x,yp,c='r')
plt.show()
#mean absolute error
print(np.abs(y - yp).mean())
#mean squared error
print(((y-yp)**2).mean())

TV = adv[['TV']]
sales = adv[['sales']]

from sklearn import linear_model
lmodel = linear_model.LinearRegression()

lmodel.fit(TV,sales)
print('Slope',lmodel.coef_)
print('Intercept',lmodel.intercept_)

p_sales = lmodel.predict(TV)

from sklearn import metrics
print('MAE',metrics.mean_absolute_error(sales,p_sales))
print('MSE',metrics.mean_squared_error(sales,p_sales))

TVR = adv[['TV','radio']]
sales = adv[['sales']]

from sklearn import linear_model
lmodel2 = linear_model.LinearRegression()

lmodel2.fit(TVR,sales)
print('Slope',lmodel2.coef_)
print('Intercept',lmodel2.intercept_)

p_sales = lmodel2.predict(TVR)

from sklearn import metrics
print('MAE',metrics.mean_absolute_error(sales,p_sales))
print('MSE',metrics.mean_squared_error(sales,p_sales))


TVRN = adv[['TV','radio','newspaper']]
sales = adv[['sales']]

from sklearn import linear_model
lmodel3 = linear_model.LinearRegression()

lmodel3.fit(TVRN , sales)
print('Slope',lmodel3.coef_)
print('Intercept',lmodel3.intercept_)

p_sales = lmodel3.predict(TVRN)

from sklearn import metrics
print('MAE',metrics.mean_absolute_error(sales,p_sales))
print('MSE',metrics.mean_squared_error(sales,p_sales))

T = adv[['TV','radio','newspaper','sales']]
print(T.corr())

p1 = lmodel.predict(adv[['TV']])
p2 = lmodel2.predict(adv[['TV','radio']])
p3 = lmodel3.predict(adv[['TV','radio','newspaper']])
print(np.hstack((adv[['sales']].values,p1,p2,p3)))