import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import OneClassSVM


from sklearn.metrics import precision_score, recall_score, f1_score


import joblib



df = pd.read_csv("creditcard.csv")

X = df.iloc[:, 1:-1].to_numpy()
y = df.iloc[:, -1:].to_numpy().ravel()


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=hiden_layer, random_state=1)

# LogisticRegression is able to give back fraud detection
# clf = LogisticRegression(solver='lbfgs', max_iter=1000)

# Giving better results than LogisticRegression
clf = RandomForestClassifier(n_estimators=100, random_state=42, class_weight="balanced")

# Gets the same score as random forest, but takes much longer
# clf = OneClassSVM(kernel="rbf", nu=0.05)


clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

# TP is true positive, as in a prediction of fraud when there is fraud
# FP is false positive, as in a prediction of fraud when there is no fraud
# TN is true negative, as in a prediction of no fraud when there is no fraud
# FN is false negative, as in a prediction of no fraud when there is fraud

# Precision
# TP / (TP + FP)
# Tells how many predicted frauds were frauds

# Recall 
# TP / (TP + FN)
# Tells how many frauds detected were correctly detected as frauds

# F1 score
# 2 * ( (Precision * Recall) / (Precision + Recall) )

precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1_score = f1_score(y_test, y_pred)


print("Precision: ", precision, "\nRecall: ", recall, "\nF1 score:", f1_score)


# This is just to save the model rather than waisting time and resources retraining it every time
joblib.dump(clf, 'model.pkl')  
