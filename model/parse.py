import keras
import os
import sys
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn import preprocessing

energy_data = os.path.abspath('../data/recs2009_public.csv')
columns = 'columns.txt'

INPUT = [
'TOTCSQFT',
'ACROOMS',
'BEDROOMS',
'WASHLOAD',
'USECENAC',
'NCOMBATH',
'TYPEHUQ',
'TEMPHOME',
'CENACHP',
'TEMPNITEAC',
'AGECDRYER',
'NAPTFLRS',
'SWIMPOOL',
'NUMCFAN',
'MAINTAC',
'COOLTYPE'
]

#INPUT = ['YEARMADE', 'BEDROOMS', 'SIZRFRI1', 'TVCOLOR', 'TEMPHOME'] #Input Vars
OUTPUT = ['KWH'] #Total Energy consumed in KWH
TRAIN_ENTRIES = 9000 #Remainder is test (12083 Total)
df = pd.read_csv(energy_data, low_memory=False)

trainX = df[INPUT][0:TRAIN_ENTRIES]
testX = df[INPUT][TRAIN_ENTRIES:]

trainY = df[OUTPUT][0:TRAIN_ENTRIES]
testY = df[OUTPUT][TRAIN_ENTRIES:]

#Normalize all values in array to between 0 and 1
def normalize(rawpoints, high=1.0, low=0.0):
    mins = np.min(rawpoints, axis=0)
    maxs = np.max(rawpoints, axis=0)
    rng = maxs - mins
    return (rawpoints - mins) / (maxs - mins)

#Return normalized values back to original
def denormalize(original, target):
    mins = np.min(original, axis=0)
    maxs = np.max(original, axis=0)

    return target * (maxs - mins) + mins

#Construct Neural Network model
def createModel(optimizer='sgd'):
    model = Sequential()

    model.add(Dense(7, input_dim=16, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(loss='mean_squared_error', optimizer=optimizer)

    return model

#Normalize data
trainXScaled = preprocessing.normalize(trainX)
trainYScaled = preprocessing.normalize(trainY)

testXScaled = preprocessing.normalize(testX)
testYScaled = preprocessing.normalize(testY)

#Initialize and train model
model = createModel()
model.fit(trainXScaled, trainYScaled, batch_size=2, epochs=10, verbose=1)

#Predict and output results
results = model.predict(testXScaled, verbose=1)
length = len(testY)
sum = 0
for index in range(length):
    output = testY.values[index][0]
    prediction = denormalize(testY, results[index]).item()
    sum += abs(output - prediction)

print('Average Error: ', sum / length)
print(model.summary())
