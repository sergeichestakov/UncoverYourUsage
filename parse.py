import keras
import os
import sys
import pandas as pd

energy_data = './data/recs2009_public.csv'

df = pd.read_csv(energy_data, low_memory=False)
print(df)
from keras.wrappers.scikit_learn import KerasClassifier

import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation

'''
trainX = df[df.columns[0:14][0:1000]]
testX = df[df.columns[0:14][1000:]]

trainY = df[df.columns[15]][0:1000]
testY = df[df.columns[15]][1000:]



def modelx(optimizer="adam"):
    model = Sequential()
    model.add(Dense(64, input_dim=14, activation='relu'))
    model.add(Dropout(0.02))
    model.add(Dense(32,activation="softmax"))
    model.add(Dropout(0.02))
    model.add(Dense(10,activation="relu"))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(loss='binary_crossentropy',
                  optimizer=optimizer,
                  metrics=['accuracy'])
    return model
    
from sklearn.model_selection import GridSearchCV
parameters = {'optimizer'😞'sgd', 'adam','adagrad','rmsprop','adadelta')}
clf = GridSearchCV(modelx,parameters)
modelx.fit(np.array(trainX), trainY2, batch_size=25, epochs=100,verbose=1)
'''
