import pandas as pd
import re as re
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
df1=pd.read_csv("home_train.csv")
df2=pd.read_csv("home_test.csv")
test=pd.DataFrame()
test['Id']=df2['Id']
f=[df1,df2]
#print(data.groupby(['Utilities']).SalePrice.mean())
for data in f:
    data.SaleCondition=data.SaleCondition.map({'Abnorml':0,'AdjLand':1,'Alloca':2,'Family':3,'Normal':4,'Partial':5})
    data.MSZoning=data.MSZoning.map({'C (all)':0,'FV':1,'RH':2,'RL':3,'RM':4})
    data.GarageType=data.GarageType.map({'2Types':0,'Attchd':1,'Basment':2,'BuiltIn':3,'CarPort':4,'Detchd':5})
    data.CentralAir=data.CentralAir.map({'N':0,'Y':1})
    data.PavedDrive=data.PavedDrive.map({'N':0,'Y':1})
    data.LotShape=data.LotShape.map({'IR1':0,'IR2':1,'IR3':2,'Reg':3})
    data.LandContour=data.LandContour.map({'Bnk':0,'HLS':1,'Low':2,'Lv1':3})
    data.Functional=data.Functional.map({'Maj1':0,'Maj2':1,'Min1':2,'Min2':3,'Sev':4,'Typ':5})
    data.SaleType=data.SaleType.map({'COD':0,'CWD':1,'Con':2,'ConLD':3,'ConLI':4,'ConLw':5,'New':6,'Oth':7,'WD':8})
    data.GarageCond=data.GarageCond.map({'Ex':0,'Fa':1,'Gd':2,'Po':3,'TA':4})
    data.GarageQual=data.GarageQual.map({'Ex':0,'Fa':1,'Gd':2,'Po':3,'TA':4})
    data.ExterQual=data.ExterQual.map({'Ex':0,'Fa':1,'Gd':2,'Po':3,'TA':4})
    data.ExterCond=data.ExterCond.map({'Ex':0,'Fa':1,'Gd':2,'Po':3,'TA':4})
    data.BsmtQual=data.BsmtQual.map({'Ex':0,'Fa':1,'Gd':2,'Po':3,'TA':4})
    data.BsmtCond=data.BsmtCond.map({'Ex':0,'Fa':1,'Gd':2,'Po':3,'TA':4})
    data.HeatingQC=data.HeatingQC.map({'Ex':0,'Fa':1,'Gd':2,'Po':3,'TA':4})
    data.KitchenQual=data.KitchenQual.map({'Ex':0,'Fa':1,'Gd':2,'Po':3,'TA':4})
    data.Electrical=data.Electrical.map({'FuseA':0,'FuseB':1,'FuseP':2,'Mix':3,'SBrkr':4})
    data.YrSold=data.YrSold.map({'2006':0,'2007':1,'2008':2,'2009':3,'2010':4,})
    data.FireplaceQu=data.FireplaceQu.map({'Ex':0,'Fa':1,'Gd':2,'Po':3,'TA':4})
    data.Street=data.Street.map({'Grvl':0,'Pave':1})
    data.Alley=data.Alley.map({'Grvl':0,'Pave':1})
    data.LandContour=data.LandContour.map({'Bnk':0,'HLS':1,'Low':2,'Lv1':3})
    data.Utilities=data.Utilities.map({'AllPub':0,'NoSeWa':1})
    
    for c in data.columns:
        data[c].fillna(value=10,inplace=True)
y=df1['SalePrice']
x=df1.drop(["Id",'SalePrice','YearBuilt','YearRemodAdd','GarageYrBlt','YrSold','FireplaceQu','GarageFinish','GrLivArea','RoofMatl','Heating','BsmtExposure','BsmtFinType1','RoofStyle','BsmtFinType2','Exterior1st','Exterior2nd','MasVnrType','Condition2','BldgType','HouseStyle','LotConfig','LandSlope','Neighborhood','Condition1','Foundation','PoolQC','Fence','MiscFeature'],axis=1)


from sklearn.ensemble import RandomForestClassifier
dmodel = RandomForestClassifier()
dmodel.fit(x,y)
print(dmodel.score(x,y))
t=df2.drop(["Id",'YearBuilt','YearRemodAdd','GarageYrBlt','YrSold','FireplaceQu','GarageFinish','GrLivArea','RoofMatl','Heating','BsmtExposure','BsmtFinType1','RoofStyle','BsmtFinType2','Exterior1st','Exterior2nd','MasVnrType','Condition2','BldgType','HouseStyle','LotConfig','LandSlope','Neighborhood','Condition1','Foundation','PoolQC','Fence','MiscFeature'],axis=1)
yPred=dmodel.predict(t)
yPred=pd.DataFrame(yPred)
test['SalePrice']=yPred[0]
print(test)