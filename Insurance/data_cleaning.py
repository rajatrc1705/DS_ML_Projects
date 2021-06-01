# -*- coding: utf-8 -*-
"""
Created on Mon May 31 10:56:55 2021

@author: rajat
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('insurance.csv')

print(data.info())

data.columns

# get dummies for categorical data
data_dum = pd.get_dummies(data)

# selecting the feature and target columns
X = data_dum.drop('charges', axis=1)
y = data_dum[['charges']]

# train test split, we will take split ratio as 75-25
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

# multiple linear regression
import statsmodels.api as sm

X_sm = X = sm.add_constant(X)
model = sm.OLS(y, X_sm)
model.fit().summary()

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

regressor = LinearRegression()
regressor.fit(X_train, y_train)

# cross validation
np.mean(cross_val_score(regressor, X_train, y_train, scoring='neg_mean_absolute_error'))

# we are off by aroung 4500 dollars.



