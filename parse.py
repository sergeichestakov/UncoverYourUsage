import keras
import os
import sys
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.wrappers.scikit_learn import KerasClassifier

energy_data = './data/recs2009_public.csv'

INPUT = ['YEARMADE', 'BEDROOMS', 'SIZRFRI1', 'TVCOLOR', 'TEMPHOME']
OUTPUT = 'TOTALBTU'
TRAIN_ENTRIES = 9000 #Remainder is test (12083 Total)
df = pd.read_csv(energy_data, low_memory=False)
print(df)

trainX = df[INPUT][0:TRAIN_ENTRIES]
testX = df[INPUT][TRAIN_ENTRIES:]
print(trainX)
print(testX)
trainY = df[OUTPUT][0:TRAIN_ENTRIES]
testY = df[OUTPUT][TRAIN_ENTRIES:]
print(trainY)
print(testY)

def createModel(optimizer="adam"):
    model = Sequential()
    model.add(Dense(64, input_dim=5, activation='relu'))
    model.add(Dropout(0.02))
    model.add(Dense(32,activation="softmax"))
    model.add(Dropout(0.02))
    model.add(Dense(10,activation="relu"))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(loss='mse',
                  optimizer=optimizer,
                  metrics=['accuracy'])
    return model

model = createModel()
model.fit(np.array(trainX), trainY, batch_size=10, epochs=100,verbose=1)
