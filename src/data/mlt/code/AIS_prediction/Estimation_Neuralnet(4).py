"""
Created on Tue Jan 26 12:11:46 2021

@author: Steffen Gans
"""

"""
Created on Sat Jan 23 18:10:20 2021

@author: Steffen Gans
"""


import os 
import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras import layers
from matplotlib.pyplot import savefig


os.getcwd()
os.chdir('C:\\Users\\Steffen Gans\\Documents\\Projects\\Export-Prediction')



df = pd.read_csv("exports_ifw_mly_norm.csv")


data = df
# delete unnecessary column
del data['Unnamed: 0']
data.head()


# set key
date_time_key = "timestamp"


# preprocessing
split_fraction = 0.8
train_split = int(split_fraction * int(df.shape[0]))
step = 1

past = 3
future = 1
learning_rate = 0.001
batch_size = 1
epochs = 100

# select features (but we use all)
features = data
features.index = data[date_time_key]
del features['timestamp']


features = pd.DataFrame(features)
#features.head()

# split into train and validation set
train_data = features.iloc[0 : train_split - 1]
val_data = features.iloc[train_split:]


## some time series stuff
start = past + future
end = start + train_split

### defining x and y on training set
x_train = train_data[[column for column in train_data]].values
y_train = features.iloc[start:end, 0:1]


sequence_length = int(past / step)

# dataset_train as keras object
dataset_train = keras.preprocessing.timeseries_dataset_from_array(
    x_train,
    y_train,
    sequence_length=sequence_length,
    sampling_rate=step,
    batch_size=batch_size,
)

x_end = len(val_data) - past - future

label_start = train_split + past + future

### defining x and y on validation set
x_val = val_data.iloc[:x_end][[column for column in val_data]].values
y_val = features.iloc[label_start:, 0:1]

# dataset_val as keras object
dataset_val = keras.preprocessing.timeseries_dataset_from_array(
    x_val,
    y_val,
    sequence_length=sequence_length,
    sampling_rate=step,
    batch_size=batch_size,
)

for batch in dataset_train.take(1):
    inputs, targets = batch
   
print("Input shape:", inputs.numpy().shape)
print("Target shape:", targets.numpy().shape)


# training
inputs = keras.layers.Input(shape=(inputs.shape[1], inputs.shape[2]))
lstm_out = keras.layers.LSTM(32)(inputs)
dense_out = keras.layers.Dense(10)(lstm_out)
outputs = keras.layers.Dense(1)(dense_out)

model = keras.Model(inputs=inputs, outputs=outputs)
model.compile(optimizer=keras.optimizers.Adam(learning_rate=learning_rate), metrics = ['mae'], loss="mse")
model.summary()                            

# ModelCheckPoint callback, to save checkpoints and early stoppping if validation
# does not improve any longer:
path_checkpoint = "model_checkpoint.h5"
es_callback = keras.callbacks.EarlyStopping(monitor="val_loss", min_delta=0, patience=5)

modelckpt_callback = keras.callbacks.ModelCheckpoint(
    monitor="val_loss",
    filepath=path_checkpoint,
    verbose=1,
    save_weights_only=True,
    save_best_only=True,
)

history = model.fit(
    dataset_train,
    epochs=epochs,
    validation_data=dataset_val,
    callbacks=[es_callback, modelckpt_callback], #es_callback, for early stops!
)



### visualize loss
def visualize_loss(history, title):
    loss = history.history["loss"]
    val_loss = history.history["val_loss"]
    epochs = range(len(loss))
    plt.figure()
    plt.plot(epochs, loss, "b", label="Training loss")
    plt.plot(epochs, val_loss, "r", label="Validation loss")
    plt.title(title)
    plt.xlabel("Epochs")
    plt.ylabel("Loss")
    plt.legend()
    plt.show()


visualize_loss(history, "Training and Validation Loss")

predictions = model.predict(dataset_train)
y_train = y_train[1:]

#visualization of train set
def visualize_predictions(title):
    true = y_train
    predicted = predictions
    time = range(len(predictions))
    #plt.xticks(range(len(y_va)), y_val.index.values )
    plt.figure()
    plt.xticks(range(len(y_train)), y_train.index.values )
    plt.plot(time, true, "b", label="True")
    plt.plot(time, predicted, "r", label="predicted")
    plt.title(title)
    plt.xlabel("Time")
    plt.ylabel("Value (Normalized)")
    plt.legend()
    plt.show()


plot = visualize_predictions("True values vs. estimated")

#plot.savefig(fname = "plot.png")


predictions = model.predict(dataset_val)
#y_val = y_val[1:]

# visualization of val set
def visualize_predictions(title):
    true = y_val
    predicted = predictions
    time = range(len(predictions))
    #plt.xticks(range(len(y_va)), y_val.index.values )
    plt.figure()
    plt.xticks(range(len(y_val)), y_val.index.values )
    plt.plot(time, true, "b", label="True")
    plt.plot(time, predicted, "r", label="predicted")
    plt.title(title)
    plt.xlabel("Time")
    plt.ylabel("Value (Normalized)")
    plt.legend()
    plt.show()


plot = visualize_predictions("True values vs. estimated")



#### RESULTS #####

# MSE Validations set: 0.1002 