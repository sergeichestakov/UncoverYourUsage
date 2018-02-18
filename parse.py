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
OUTPUT = ['KWH'] #Total Energy consumed in BTU
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
    return (rawpoints - mins) / (maxs - mins)

def denormalize(original, target):
    mins = np.min(original, axis=0)
    maxs = np.max(original, axis=0)

    return target * (maxs - mins) + mins

def createModel(optimizer="adam"):
    model = Sequential()
    model.add(Dense(3, input_dim=5, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(loss='mean_squared_error', optimizer=optimizer)

    return model

trainXScaled = normalize(trainX)
trainYScaled = normalize(trainY)

testXScaled = normalize(testX)
testYScaled = normalize(testY)

model = createModel()
model.fit(trainXScaled, trainYScaled, batch_size=25, epochs=3,verbose=1)

results = model.predict(testXScaled, verbose=1)
for index in range(len(testY)):
    output = testY.values[index][0]
    prediction = denormalize(testY, results[index]).item()
    print('Index ', index)
    print('OUTPUT: ', output)
    print('PREDICTION: ', prediction)
