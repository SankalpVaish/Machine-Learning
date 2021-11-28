import pandas as pd
import re as re
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
df1=pd.read_csv("train.csv")
df2=pd.read_csv("test.csv")
z=df1
df1['Age']=df1['Age'].fillna(df1['Age'].mean())

pd.set_option('display.max_columns', None)
full_data=[df1,df2]
def get_title(name):
	title_search = re.search(' ([A-Za-z]+)\.', name)
	# If the title exists, extract and return it.
	if title_search:
		return title_search.group(1)
	return ""

for dataset in full_data:
    dataset['Title'] = dataset['Name'].apply(get_title)
    
for dataset in full_data:
    dataset['Title'] = dataset['Title'].replace(['Lady', 'Countess','Capt', 'Col',\
 	'Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')
    dataset['FamilySize'] = dataset['SibSp'] + dataset['Parch'] + 1
    dataset['Title'] = dataset['Title'].replace('Mlle', 'Miss')
    dataset['Title'] = dataset['Title'].replace('Ms', 'Miss')
    dataset['Title'] = dataset['Title'].replace('Mme', 'Mrs')
print (df1[['Title', 'Survived']].groupby(['Title'], as_index=False).mean())
for dataset in full_data:
    # Mapping titles
    title_mapping = {"Mr": 1, "Miss": 2, "Mrs": 3, "Master": 4, "Rare": 5}
    dataset['Title'] = dataset['Title'].map(title_mapping)
    dataset['Title'] = dataset['Title'].fillna(0)

maped=df1.groupby(['Cabin']).Survived.mean().astype(int)
for dataset in full_data:
    dataset['Cabin'] = dataset['Cabin'].map(maped)
    dataset['Cabin'].fillna(value=2, inplace=True)
maped=df1.groupby(['Ticket']).Survived.mean().astype(int)
for dataset in full_data:
    dataset['Ticket'] = dataset['Ticket'].map(maped)
    dataset['Ticket'].fillna(value=2, inplace=True)
for dataset in full_data:
    dataset['IsAlone'] = 0
    dataset.loc[dataset['FamilySize'] == 1, 'IsAlone'] = 1
    dataset.loc[ dataset['Age'] <= 16, 'Age'] 					       = 0
    dataset.loc[(dataset['Age'] > 16) & (dataset['Age'] <= 32), 'Age'] = 1
    dataset.loc[(dataset['Age'] > 32) & (dataset['Age'] <= 48), 'Age'] = 2
    dataset.loc[(dataset['Age'] > 48) & (dataset['Age'] <= 64), 'Age'] = 3
    dataset.loc[ dataset['Age'] > 64, 'Age']  

x=df1.drop(['Name','Sex','SibSp','Parch','FamilySize'],axis=1)
x['sex']=df1['Sex'].map({'male':1, 'female':0})
x['Embarked']=df1['Embarked'].map({'C':0, 'Q':1, 'S':2})

y=df1['Survived']

