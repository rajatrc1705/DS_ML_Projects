# -*- coding: utf-8 -*-

import pandas as pd 
import numpy as np
import xgboost as xgb
from sklearn.svm import SVC
from sklearn import preprocessing, decomposition, model_selection, metrics, pipeline
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB

data = pd.read_csv('cleaned_data.csv')

X = data[['description']]
y = data[['category']]

from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(data.category.values)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data.description.values, y,  
                                                stratify=y, random_state=0, 
                                                  test_size=0.25, shuffle=True)

tfv = TfidfVectorizer(min_df=3,  max_features=None, 
            analyzer='word', token_pattern=r'\w{1,}',
            ngram_range=(1, 3), sublinear_tf=True)


# Fitting TF-IDF to training set and test set, and transforming train and test set
tfv.fit(list(X_train))
X_train_tfv =  tfv.transform(X_train) 
X_test_tfv = tfv.transform(X_test)

# Fitting a simple Logistic Regression on TFIDF
clf = LogisticRegression(C=1.0)
clf.fit(X_train_tfv, y_train)
predictions = clf.predict_proba(X_test_tfv)

# convert predictions to required formatting 
def generateDifferent(predictions):
    
    y_preds = list()
    for i in range(len(predictions)):
        # print(predictions[i])
        m = max(predictions[i])
        y_preds.append(list(predictions[i]).index(m))
    
    return y_preds

from sklearn.metrics import log_loss, f1_score

print("Logistic Regression")
print("Log Loss: {:.5f}".format(log_loss(y_test, predictions)))
print("F1 Score: {:.5f}".format(f1_score(y_test, generateDifferent(predictions), average='weighted')))
print("#"*10)

# naive bayes
mnb = MultinomialNB(fit_prior=True)
mnb.fit(X_train_tfv, y_train)
predictions_mnb = mnb.predict_proba(X_test_tfv)

print("Naive Bayes")
print("Log Loss: {:.5f}".format(log_loss(y_test, predictions_mnb)))
print("F1 Score: {:.5f}".format(f1_score(y_test, generateDifferent(predictions_mnb), average='weighted')))
print("#"*10)

# bagging classifier with Decision Tree as base estimator
from sklearn.ensemble import BaggingClassifier
bg_classifier = BaggingClassifier(n_jobs=-1)
bg_classifier.fit(X_train_tfv, y_train)
predictions_bg = bg_classifier.predict_proba(X_test_tfv)

print("Bagging Classifier using Decision Tree as base estimator")
print("Log Loss: {:.5f}".format(log_loss(y_test, predictions_bg)))
print("F1 Score: {:.5f}".format(f1_score(y_test, generateDifferent(predictions_bg), average='weighted')))
print("#"*10)


# bagging classifier with SVC as base estimator
from sklearn.ensemble import BaggingClassifier
bg_classifier = BaggingClassifier(base_estimator=SVC(), n_jobs=-1)
bg_classifier.fit(X_train_tfv, y_train)
predictions_bg = bg_classifier.predict_proba(X_test_tfv)

print("Bagging Classifier using Decision Tree as base estimator")
print("Log Loss: {:.5f}".format(log_loss(y_test, predictions_bg)))
print("F1 Score: {:.5f}".format(f1_score(y_test, generateDifferent(predictions_bg), average='weighted')))
print("#"*10)