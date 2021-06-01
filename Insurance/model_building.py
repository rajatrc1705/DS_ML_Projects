# -*- coding: utf-8 -*-
"""
Created on Mon May 31 10:56:55 2021

@author: rajat
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
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

from sklearn.linear_model import LinearRegression, Lasso
from sklearn.model_selection import cross_val_score, GridSearchCV, RepeatedKFold

regressor = LinearRegression()
regressor.fit(X_train, y_train)

accuracy_lr = np.mean(cross_val_score(regressor, X_train, y_train, scoring='neg_mean_absolute_error', cv=10))
print("Accuracy : {:.2f}".format(accuracy_lr*-1))

# we are off by aroung 4200 dollars.

# now we try lasso regression model
clf = Lasso(alpha=0.1, fit_intercept=True, normalize=True)
accuracy_clf = np.mean(cross_val_score(clf, X_train, y_train, scoring='neg_mean_absolute_error', cv=10))
print("Accuracy : {:.2f}".format(accuracy_clf*-1))

# we try different values of alpha for the Lasso regressor, hyperparameter tuning 
alpha = list()
error = list()

for i in range(1, 100):
    alpha.append(i/100)
    clf = Lasso(alpha=i/100)
    err = np.mean(cross_val_score(clf, X_train, y_train, scoring='neg_mean_absolute_error', cv=10))
    error.append(err)

plt.plot(alpha, error)

clf = Lasso(alpha=0.2)
accuracy_clf = np.mean(cross_val_score(clf, X_train, y_train, scoring='neg_mean_absolute_error', cv=10))

print("Accuracy : {:.2f}".format(accuracy_clf*-1))
# changing the value of alpha is not having much effect on the model.
# there is no significant improvement by using Lasso

# random forrest regression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

rfr = RandomForestRegressor()

# k-fold cross validation
accuracies_rfr = cross_val_score(rfr, X_train, y_train.values.ravel(), scoring='neg_mean_absolute_error', cv=10)
print("Accuracy: {:.2f}".format(-1*accuracies_rfr.mean()))
print("Standard Deviation: {:.2f}".format(accuracies_rfr.std()))


# there is a marked improvement by using Random Forest, we are now off by about $ 2600

# hyperparameter tuning using the grid search technique for random forest regressor
parameters = {'n_estimators': range(100, 200, 10), 
               'criterion': ['mae', 'mse'],
               }
               
grid_search = GridSearchCV(rfr, parameters, scoring='neg_mean_absolute_error', cv=10, n_jobs=-1)
grid_search.fit(X_train, y_train.values.ravel()) 
best_accuracy = grid_search.best_score_
best_parameters = grid_search.best_params_
print("Best Accuracy: {:.2f}".format(best_accuracy*-1))
print("Best Parameters: {}".format(best_parameters))              

# the best criterion for random forest turns out to be mse, which actually is the default
# the number of estimators have their best value at 120

# using Gradient Boosted Random Forests

est = GradientBoostingRegressor(n_estimators=120, learning_rate=0.1, random_state=0, loss='huber')
est.fit(X_train, y_train.values.ravel())
n_scores = cross_val_score(est, X_train, y_train.values.ravel(), scoring='neg_mean_absolute_error', cv=cv, n_jobs=-1)
print('MAE: {:.3f} {:.3f}'.format(n_scores.mean()*-1, n_scores.std()))
# the gradient boosted random forests turns out to be way better than any other model so far
# it is giving an MAE of about $ 1800

# testing all the models

regressor.fit(X_train, y_train.values.ravel())
clf = Lasso(alpha=0.2)
clf.fit(X_train, y_train.values.ravel())
rfr = RandomForestRegressor(criterion='mse', n_estimators=120)
rfr.fit(X_train, y_train.values.ravel())
est.fit(X_train, y_train.values.ravel())

lr_pred = regressor.predict(X_test)
clf_pred = clf.predict(X_test)
rfr_pred = rfr.predict(X_test)
gbrf_pred = est.predict(X_test)

from sklearn.metrics import mean_absolute_error

mae_lr = mean_absolute_error(y_test, lr_pred)
mae_clf = mean_absolute_error(y_test, clf_pred)
mae_rfr = mean_absolute_error(y_test, rfr_pred)
mae_gbrf = mean_absolute_error(y_test, gbrf_pred)

print("MAE for Linear Regression: {:.2f}".format(mae_lr))
print("MAE for Lasso Regression: {:.2f}".format(mae_clf))
print("MAE for Random Forrest Regression: {:.2f}".format(mae_rfr))
print("MAE for Gradient Boosted Random Forrest: {:.2f}".format(mae_gbrf))





