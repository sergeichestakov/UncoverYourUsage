import keras
import os
import sys
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.wrappers.scikit_learn import KerasClassifier

energy_data = './data/recs2009_public.csv'

INPUT = ['YEARMADE', 'BEDROOMS', 'SIZRFRI1', 'TVCOLOR', 'TEMPHOME'] #Input Vars
OUTPUT = ['TOTALBTU'] #Total Energy consumed in BTU
TRAIN_ENTRIES = 9000 #Remainder is test (12083 Total)
df = pd.read_csv(energy_data, low_memory=False)

trainX = df[INPUT][0:TRAIN_ENTRIES]
testX = df[INPUT][TRAIN_ENTRIES:]

trainY = df[OUTPUT][0:TRAIN_ENTRIES]
testY = df[OUTPUT][TRAIN_ENTRIES:]

def normalize(rawpoints, high=1.0, low=0.0):
    mins = np.min(rawpoints, axis=0)
    maxs = np.max(rawpoints, axis=0)
    rng = maxs - mins
    return high - (((high - low) * (maxs - rawpoints)) / rng)

def createModel(optimizer="adam"):
    model = Sequential()
    model.add(Dense(60, input_dim=5, activation='relu'))
    model.add(Dropout(0.02))
    model.add(Dense(32,activation="softmax"))
    model.add(Dropout(0.02))
    model.add(Dense(10,activation="relu"))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(loss='mean_squared_error', optimizer=optimizer)
               
    return model

trainXScaled = normalize(trainX)
trainYScaled = normalize(trainY)

model = createModel()
model.fit(trainXScaled, trainYScaled, batch_size=3, epochs=10,verbose=1)
