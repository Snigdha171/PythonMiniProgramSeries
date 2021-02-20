# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 23:17:57 2021

@author: Prachi Prakash
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn import linear_model
import pickle

# Laoding the data
advertising = pd.read_csv('Advertising.csv')

# Checking the data 
advertising.describe()

# Checking for null values
advertising.isnull().any()

# Diving the data for train and test
x = advertising[['Newspaper', 'Radio', 'TV']]
y = advertising[['Sales']]

# Scaling the variables
sc = StandardScaler()
X = sc.fit_transform(x)

# Splitting the data into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y,random_state = 100,test_size=0.2)

# Creating a linear model and fitting the train data
lrm = linear_model.LinearRegression()
lrm.fit(X_train,y_train)

# Building Predictions
y_pred = lrm.predict(X_train)

# Checking the R-squared
print(r2_score(y_train, y_pred))

# Printing the predictor coefficient
print(lrm.coef_)

# After checking the model and obtaining satisfactory result, store the model in pickle file
pickle.dump(lrm, open('lrm_advertising.pkl','wb'))

print(lrm.predict([[20, 5, 5]]))

prediction_output = lrm.predict([[20, 5, 5]])
output = prediction_output[0]
print(output[0])
print(round(output[0], 2))
print(type(output))