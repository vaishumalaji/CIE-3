# -*- coding: utf-8 -*-
"""CIE-3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11QJfvwKZVSUzIdP2e0ObZw-K5BSEk8_H

## **Import the Libraries**
"""

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

"""**Loading Dataset**"""

iris=load_iris()
x=iris.data
y=iris.target

"""**Converting the dataset into the Dataframe**"""

df=pd.DataFrame(data=x,columns=iris.feature_names)
df['species']=pd.Categorical.from_codes(y,iris.target_names)
print(df['species'])
print(df.describe())
print(df.shape)
print(df.info())
print(df['species'].value_counts())

"""**Checking the missing values**"""

print(df.isnull().sum())

"""**Hence, their is no missing values so their is no necessery to do preprocessing **

**Data Splitting**
"""

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=4)
print(x_train)
print(y_train)

"""**Creating the Model**"""

clf=DecisionTreeClassifier(random_state=42)
clf.fit(x_train,y_train)

"""**Predicting**"""

yperd=clf.predict(x_test)
yperd

"""**Calculating then accuracy score**"""

accuracy=accuracy_score(y_test,yperd)
print("Accuracy Score=",accuracy)