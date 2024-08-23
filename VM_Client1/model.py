import numpy as np
from tensorflow.keras.layers import Input, LSTM, GRU, Bidirectional, Dense
from tensorflow.keras.models import Model
import tensorflow.keras.backend as K

# Define the simple LSTM model
def simple_model_LSTM(input_shape, units):
    inputs = Input(shape=input_shape)
    lstm_out = LSTM(units)(inputs)
    output = Dense(1)(lstm_out)
    model = Model(inputs=inputs, outputs=output)
    return model

# Define the simple GRU model
def simple_model_GRU(input_shape, units):
    inputs = Input(shape=input_shape)
    gru_out = GRU(units)(inputs)
    output = Dense(1)(gru_out)
    model = Model(inputs=inputs, outputs=output)
    return model

# Define the simple BiLSTM model
def simple_model_BiLSTM(input_shape, units):
    inputs = Input(shape=input_shape)
    bilstm_out = Bidirectional(LSTM(units))(inputs)
    output = Dense(1)(bilstm_out)
    model = Model(inputs=inputs, outputs=output)
    return model

# Function to create dataset for time series forecasting
def create_dataset(dataset, time_step=1):
    dataX, dataY = [], []
    for i in range(len(dataset) - time_step - 1):
        a = dataset[i:(i + time_step), 0]
        dataX.append(a)
        dataY.append(dataset[i + time_step, 0])
    return np.array(dataX), np.array(dataY)

