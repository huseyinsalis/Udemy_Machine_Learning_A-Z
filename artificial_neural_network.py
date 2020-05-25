# -*- coding: utf-8 -*-
"""
Created on Tue May 19 22:13:11 2020
 ANN example
@author: user1
"""

import numpy as np
import pandas as pd
import tensorflow as tf

dataset = pd.read_csv('Churn_Modelling.csv')
X = dataset.iloc[:, 3 : 13].values
y = dataset.iloc[:, -1].values

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [1,2])], remainder='passthrough')
X1 = np.array(ct.fit_transform(X))

# Remove first and third column to avoid from dummy variable trap

X = X1[:,1:]
idxs = list(range(0, 12))
idxs.pop(2) #this removes 2 from the list
X = X[:, idxs]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# ANN

import keras

from keras.models import Sequential
from keras.layers import Dense

#initilize ANN
classifier = Sequential()

#add first layer and hidden layer

classifier.add(Dense(6, input_shape=(11,) ,kernel_initializer='uniform', activation = 'relu'))

