# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 13:50:25 2020

@author: user1
"""
#Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:-1].values
y = dataset.iloc[:, -1].values
y_scaled= y.reshape(-1,1)

#Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
sc_X.fit(X)
sc_y.fit(y_scaled)
X = sc_X.transform(X)
y_scaled = sc_y.transform(y_scaled)

#Training the SVR model on the whole dataset
from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf')
regressor.fit(X, y_scaled)

#Predicting a new result
inp=np.array([[6.5]])
inp2=inp.reshape(-1,1)
Scaled_input=sc_X.transform(inp2)
y_pred = regressor.predict(Scaled_input)
y1=np.array(y_pred)
y2=inp.reshape(-1,1)
y_pred2 = sc_y.inverse_transform(y2)

#Visualising the SVR results
plt.scatter(X, y, color = 'red')
plt.plot(X, regressor.predict(X), color = 'blue')
plt.title('Truth or Bluff (SVR)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()