#!/usr/bin/env python
# coding: utf-8
import urllib.request as req
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import pandas as pd


def getIris():
    # url = "https://raw.githubusercontent.com/pandas-dev/pandas/master/pandas/tests/data/iris.csv"
    savefile = 'iris.csv'
    # req.urlretrieve(url, savefile)
    csv = pd.read_csv(savefile)
    y = csv.loc[:, 'Name']
    x = csv.loc[:, ['SepalLength', 'SepalWidth', 'PetalLength',  'PetalWidth']]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, train_size=0.8, shuffle=True)
    clf = SVC()
    clf.fit(x_train, y_train)
    y_pred = clf.predict(x_test)
    return accuracy_score(y_test, y_pred)

