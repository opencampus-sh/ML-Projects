# -*- coding: utf-8 -*-
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
#from tensorflow.keras.preprocessing.sequence import pad_sequences
#from sklearn.preprocessing import StandardScaler
#import pandas as pd
import matplotlib.pyplot as plt



os.getcwd()
os.chdir('C:\\Users\\Steffen Gans\\Documents\\Projects\\Export-Prediction')


# load data.table
#df = pd.read_csv("model.matrix_new.csv")
#df = pd.read_csv("exports_ifw_final.csv")
df = pd.read_csv("model.matrix.csv")

data = df
# delete unnecessary column
del data['Unnamed: 0']
#del data['V1']
#del data['year']
#del data['month']
#del data['mday']
# define target values
#target = df.pop('ausfuhr_dollar')
data.head()
# sort and lag values
#data = data.sort_values(by= 'timestamp')
#data = data.set_index('timestamp')

#data = data.shift(periods =30)
#data = data[30:10314180]


###### fromw weather website

titles = [
    "ausfuhr_dollar",
    "imo",
    "speed",
    "course",
    "latitude",
    "longitude",
    "length",
    "draught",
    "width",
    "sum.ships"
]

feature_keys = [
     "ausfuhr_dollar",
    "imo",
    "speed",
    "course",
    "latitude",
    "longitude",
    "length",
    "draught",
    "width",
    "sum.ships"
]

colors = [
    "blue",
    "orange",
    "green",
    "red",
    "purple",
    "brown",
    "pink",
    "gray",
    "olive",
    "cyan",
]

# oder timestamp?
date_time_key = "timestamp"


#def show_raw_visualization(data):
#    time_data = data[date_time_key]
#    fig, axes = plt.subplots(
#        nrows=7, ncols=2, figsize=(15, 20), dpi=80, facecolor="w", edgecolor="k"
#    )
#    for i in range(len(feature_keys)):
#        key = feature_keys[i]
#        c = colors[i % (len(colors))]
#        t_data = data[key]
#        t_data.index = time_data
#        t_data.head()
#        ax = t_data.plot(
#            ax=axes[i // 2, i % 2],
#            color=c,
#            title="{} - {}".format(titles[i], key),
#            rot=25,
#        )
#        ax.legend([titles[i]])
#    plt.tight_layout()
#
#
#show_raw_visualization(df)
#######################


# preprocessing
split_fraction = 0.80
train_split = int(split_fraction * int(df.shape[0]))
step = 1

past = 31
future = 31
learning_rate = 0.001
batch_size = 1
epochs = 50

# select features (but we use all)
#print(
#    "The selected parameters are:",
#    ", ".join([titles[i] for i in list(range(0,794))]),
#)
#selected_features = [feature_keys[i] for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
features = data
features.index = data[date_time_key]
#features.head()
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
   
#dataset = tf.keras.preprocessing.sequence.pad_sequences(
#    dataset_train, maxlen=3965, dtype="int32", padding="pre", truncating="pre", value=0.0
#)
   
print("Input shape:", inputs.numpy().shape)
print("Target shape:", targets.numpy().shape)


# training
inputs = keras.layers.Input(shape=(inputs.shape[1], inputs.shape[2]))
conv_out = keras.layers.Conv1D(filters=32, kernel_size=5, strides=1, activation="relu")(inputs)
lstm_out = keras.layers.LSTM(64)(conv_out)
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

# visualize loss
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

predictions = model.predict(dataset_val)

