import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
#Train a model to predict if a person is diabetic or non-diabetic
ch = ['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age','Outcome']
df = pd.read_csv('diabetes.csv',header=None)
df.columns=ch
X=df[['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']]
Y=df['Outcome']
xtrain,xtest,ytrain,ytest = train_test_split(X,Y,test_size=0.3,random_state=6)
model=KNeighborsClassifier(n_neighbors=8)
model.fit(xtrain,ytrain)
print(model.score(xtrain,ytrain))
print(model.score(xtest,ytest))

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

xtest_numpy = xtest.values
kmodel.predict(xtest_numpy[100].reshape(1,8))
ytest_numpy = ytest.values
ytest_numpy[100]