import pandas as pd
import numpy as np
from numpy import concatenate
import yfinance as yf
import matplotlib.pyplot as plt
from math import sqrt
from sklearn.metrics import mean_squared_error

from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout


def LSTM_train(data,timestep = 3,epochs = 15,batch_size = 50,validation_split = 0.1,train_test_split_date = '2021-09-05'):

	#Drop Date and Adj Close columns
	training_data = data.drop(['Date', 'Adj Close'], axis = 1)

	#Scale data using MinMax Scaler
	scaler = MinMaxScaler()
	training_data = scaler.fit_transform(training_data)

	#Reshape data into (samples,timesteps,features)
	X_train = [] 
	Y_train = []
	for i in range(timestep, training_data.shape[0]):
	  X_train.append(training_data[i-timestep:i])
	  Y_train.append(training_data[i,0])
	X_train, Y_train = np.array(X_train), np.array(Y_train)

	#Define LSTM Architecture
	model = Sequential() 
	model.add(LSTM(units = 32, activation = 'relu', return_sequences = True))
	model.add(Dropout(0.3)) 
	model.add(LSTM(units = 64, activation = 'relu', return_sequences = True))
	model.add(Dropout(0.4)) 
	model.add(LSTM(units = 128, activation = 'relu'))
	model.add(Dropout(0.5)) 
	model.add(Dense(units =1))

	#Compile Model
	model.compile(optimizer = 'adam', loss = 'mean_squared_error')
	history= model.fit(X_train, Y_train, epochs = epochs, batch_size =batch_size, validation_split=validation_split)

	loss = history.history['loss']
	val_loss = history.history['val_loss']
	epochs = range(len(loss))
	plt.figure()
	plt.plot(epochs, loss, 'b', label='Training loss')
	plt.plot(epochs, val_loss, 'r', label='Validation loss')
	plt.title("Training and Validation Loss")
	plt.legend()
	plt.show()

	return model,scaler



def predict(model,data_training,data_test,timestep,scaler):
	part_60_days = data_training.tail(60)
	df= part_60_days.append(data_test, ignore_index = True)
	df = df.drop(['Date', 'Adj Close'], axis = 1)

	inputs = scaler.transform(df)

	X_test = []
	Y_test = []
	for i in range(timestep, inputs.shape[0]):
	  X_test.append(inputs[i-timestep:i])
	  Y_test.append(inputs[i,0])
	X_test, Y_test = np.array(X_test), np.array(Y_test)

	Y_pred = model.predict(X_test)
	scale = 1/scaler.scale_[0]
	Y_test = Y_test*scale 
	Y_pred = Y_pred*scale

	plt.figure(figsize=(14,5))
	plt.plot(Y_test, color = 'red', label = 'Real Bitcoin Price')
	plt.plot(Y_pred, color = 'green', label = 'Predicted Bitcoin Price')
	plt.title('Bitcoin Price Prediction using RNN-LSTM')
	plt.xlabel('Time')
	plt.ylabel('Price')
	plt.legend()
	plt.show()