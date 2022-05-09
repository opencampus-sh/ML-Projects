from __future__ import absolute_import, division, print_function
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix,f1_score
import seaborn as sns
from matplotlib.pyplot import cm
import matplotlib.pyplot as plt

def plt_history(history):
    # taken and slightly modified
    # from https://machinelearningmastery.com/display-deep-learning-model-training-history-in-keras/
    epochs = range(1,len(history.history['accuracy'])+1)
    
    # summarize history for accuracy
    plt.plot(epochs,history.history['accuracy'])
    plt.plot(epochs,history.history['val_accuracy'])
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.xticks(epochs)
    plt.legend(['train', 'test'], loc='upper left')
    plt.show()
    # summarize history for loss
    plt.plot(epochs,history.history['loss'])
    plt.plot(epochs,history.history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.xticks(epochs)
    plt.legend(['train', 'test'], loc='upper left')
    plt.show()


def get_input_column_names(NN,n_bin=101):
    """ Given the NN number, this function returns the column
        names that correspond to the input for the NN.
        Input: - NN is 1 or 2
               - n_bin is the number of bins in the density 
                 plot and is only relevant if NN is 2
    """
    assert NN in [1,2],f"Error! NN must be either 1 or 2 and not NN={NN}."
    
    if NN==1: return ["SpikeShapes_"+str(i) for i in range(1,65)]
    elif NN==2: return [f"{i}" for i in range(n_bin*64)]
    

def read_input(data,NN,n_bin=101,is_test=False,x_tot_std=30.225052516123352):
    """ Reads input files.
        Input: - data is the input dataFrame
               - NN is 1 or 2
               - n_bin is the number of bins in the density 
                 plot and is only relevant if NN is 2 
               - if is_test is True, the data requires 
                 x_tot_std as input
               - x_tot_std is used for NN=1 to normalize
                 the input data
                 if is_test=False, it is first determined
    """
    
    assert NN in [1,2],f"Error! NN must be either 1 or 2 and not NN={NN}." 
    
    # get labels for the input data
    labels = get_input_column_names(NN,n_bin)
    
    # store data in numpy array
    x_tot = data[labels].to_numpy(dtype=np.float)
    
    if NN==1:
        if not is_test: 
            # determine standard deviation of test+dev data
            x_tot_std = np.std(x_tot)
            
        # normalize input
        x_tot /= x_tot_std
    elif NN==2: 
        # reshape data to enable the usage of a CNN
        x_tot  = x_tot.reshape((-1,n_bin,64))
    
    # make sure the data type is float
    x_tot=x_tot.astype(np.float)
    
    # find output labels ["SU","MU","A"]
    y_tot_labels = data["unitClass"].to_numpy()
    
    # convert labels to numbers 0, 1, and 2
    y_tot = np.zeros(y_tot_labels.shape[0])
    y_labels = ["SU","MU","A"]
    for y_label in y_labels: y_tot[y_tot_labels==y_label] = get_number_from_label(y_label)
    
    if NN==1 and not is_test: return x_tot,y_tot,x_tot_std
    else: return x_tot,y_tot


def get_channel_cluster_signals(data,channel_id,cluster_id):
    """ for a channel and selected cluster, return all signals 
        in a numpy array of shape (m,64) 
        Input: - data is a dataFrame
               - channel_id is the id of the channel
               - cluster_id is the id of the cluster
    """
    
    labels = []
    for i in range(1,65): labels.append("SpikeShapes_"+str(i))

    return data[(data["channelID"]==channel_id) & (data["clusterID"]==cluster_id)][labels].to_numpy(dtype=np.float)
        

def spike_heatmap(spikes, ax=None, x=None, log=False):
    """
    takes spikes, plots heatmap over samples and mean/std line
    Input:  - spikes is an array of shape (m,64)
            - ax is the axis of a figure
            - x is the array of time stamps of length 64
            - log=True for logarithmic heatmap
    """
    # -*- encoding: utf-8 -*-
    # slightly adjusted taken from: https://github.com/Willie-Lab/
    # Analysis_Combinato/blob/master/combinato/plot/spike_heatmap.py
    # JN 2014-12-14
    # function to plot heatmaps of clusters
 
    cmap = cm.Blues

    # idea taken from http://stackoverflow.com/a/14779462
    cmaplist = [cmap(i) for i in range(int(cmap.N/4), cmap.N)]
    # set first color to white
    cmaplist[0] = (1, 1, 1, 1)
    # set last color to black
    cmaplist[-1] = (0, 0, 0, 1)

    cmap = cmap.from_list('Custom cmap', cmaplist, cmap.N)

    spMin = spikes.min()
    spMax = spikes.max()
    spBins = np.linspace(-5., 5., 102)

    nSamp = spikes.shape[1]

    if x is None: x = range(nSamp)

    imdata = np.zeros((len(spBins) - 1, nSamp))

    for col in range(nSamp):
        data = np.histogram(spikes[:, col], bins=spBins)[0]
        if log:
            imdata[:, col] = np.log(1 + data)
        else:
            imdata[:, col] = data
    
    if ax is not None:
        ydiff = (spBins[1] - spBins[0])/2.
        extent = [x[0], x[-1], -5., 5.]

        ax.imshow(imdata,
                  cmap=cmap,
                  interpolation='hanning',
                  aspect='auto',
                  origin='lower',
                  extent=extent)

        spMean = spikes.mean(0)
        spStd = spikes.std(0)

        ax.plot(x, spMean, 'k', lw=1)
        ax.plot(x, spMean + spStd, color=(.2, .2, .2), lw=1)
        ax.plot(x, spMean - spStd, color=(.2, .2, .2), lw=1)

        ax.set_xlim((x[0], x[-1]))
    
    imdata = imdata/spikes.size
    return imdata

def plot_confusion_matrix(y_true,y_pred,settitle=None):
    cm = confusion_matrix(y_true,y_pred)
    cm_norm = cm.astype('float')/cm.sum(axis=1)[:,np.newaxis]
    df_cm = pd.DataFrame(cm_norm, index = ["SU","MU","A"],
                      columns = ["SU","MU","A"])
    
    plt.figure()
    sns.heatmap(df_cm, annot=True, cmap="Reds")
    if title is not None: plt.title(settitle)
    
    
    return cm_norm

def test_single_cluster(model,data_t,x_t,y_t,patient_number,save_figure=True,NN=1):
    if NN == 1:
        print("Single Signal Prediction:")
        model.evaluate(x_t,  y_t, verbose=2)

        y_t_predict = model.predict(x_t, verbose=2)
        plot_confusion_matrix(y_t,np.argmax(y_t_predict,axis=1),settitle=f"Patient {patient_number} - Single Spike")
        if save_figure: plt.savefig(f"./figs/confusion_NN{NN}_spike_{patient_number}.png",bbox_inches="tight",dpi=300)
        print(f"F1-score (single): {f1_score(y_t,np.argmax(y_t_predict,axis=1),average='weighted')}")
        
        print("Cluster Prediction:")
        y_t_prediction_cluster = get_accuracy_cluster_prediction(data_t,y_t_predict)
        plot_confusion_matrix(y_t,y_t_prediction_cluster,settitle=f"Patient {patient_number} - Complete Cluster")
        if save_figure: plt.savefig(f"./figs/confusion_NN{NN}_cluster_{patient_number}.png",bbox_inches="tight",dpi=300)
        print(f"F1-score (cluster): {f1_score(y_t,y_t_prediction_cluster,average='weighted')}")
    elif NN==2:
        model.evaluate(x_t,  y_t, verbose=2)

        y_t_predict = model.predict(x_t, verbose=2)
        plot_confusion_matrix(y_t,np.argmax(y_t_predict,axis=1),settitle=f"Patient {patient_number} - Complete Cluster")
        if save_figure: plt.savefig(f"./figs/confusion_NN{NN}_cluster_{patient_number}.png",bbox_inches="tight",dpi=300)
        print(f"F1-score: {f1_score(y_t,np.argmax(y_t_predict,axis=1),average='weighted')}")
        
    else: print(f"Error! Unexpected number: NN={NN}")


def get_label_from_number(y_pred):
    """ Convert number of label to SU,Mu, or A. """
    if y_pred == 0: return "SU"
    elif y_pred == 1: return "MU"
    else: return "A"

def get_number_from_label(y_pred):
    """ Convert number of label to SU,Mu, or A. """
    if y_pred == "SU": return 0
    elif y_pred == "MU": return 1
    else: return 2
    
def get_channels(data): 
    """ returns unique channel ids """
    return np.sort(data["channelID"].unique())

def get_channel_clusters(data, channel_id):
    """ returns unique cluster ids of a selected channel_id """
    return np.sort(data[(data["channelID"]==channel_id)]["clusterID"].unique())

def get_cluster_label(data,channel_id,cluster_id):
    """ returns the label of a cluster of a channel """
    
    labels = data[(data["channelID"]==channel_id) & (data["clusterID"]==cluster_id)]["unitClass"].unique()
    assert labels.size==1,f"Cluster {cluster_id} has more than one label in channel {channel_id}!"
    
    return labels[0]

def get_accuracy_cluster_prediction(data,y_prediction):
    """ Calculate the accuracy for predicting a cluster ID based on single signal IDs. """
    
    # make confusion matrix
    y_prediction_cluster = np.zeros(y_prediction.shape[0])
    
    # count correct predictions
    total_cluster_number = 0.
    correct_cluster_pred = 0.
    
    # get channel ids
    channel_ids = get_channels(data)
    
    # collect all ids for a cluster
    for channel_id in channel_ids:
        cluster_ids = get_channel_clusters(data, channel_id)
        for cluster_id in cluster_ids:
            
            # update cluster number
            total_cluster_number += 1
            
            # get indices
            indices = data[(data["channelID"]==channel_id) & (data["clusterID"]==cluster_id)].index.to_numpy()

            # get all cluster predictions from NN
            cluster_predictions = np.argmax(y_prediction,axis=1)[indices]
            
            # get most frequent prediction
            cluster_prediction = get_label_from_number(np.argmax(np.bincount(cluster_predictions)))
            
            # get true cluster label
            cluster_true = get_cluster_label(data,channel_id,cluster_id)
            
            # check if correctly assigned 
            if cluster_prediction==cluster_true: correct_cluster_pred += 1
            
            # make cluster prediction vector
            if cluster_prediction=="A": cluster_prediction=2
            if cluster_prediction=="SU": cluster_prediction=0
            if cluster_prediction=="MU": cluster_prediction=1
            y_prediction_cluster[indices] = cluster_prediction
            
    print("Cluster Accuracy = ",correct_cluster_pred/total_cluster_number)
    
    return y_prediction_cluster
    


def load_single_dataset(fpath,drop_columns=False):
    """ Load a csv dataset. """
    
    # load data
    data = pd.read_csv(fpath)
    
    # drop unused columns to save memory
    if drop_columns: data = data.drop(columns=['bundleID', 'region','threshold','timeStamps','detectionLabel'])
    
    return data

def load_train_dev_testx4(data,data_t1,data_t2,data_t3,data_t4,
                          save_path='./data/train_dev_set.csv',
                          ignore_train_dev=False,ignore_test=False):
    """ Load data files for train+dev and four tests. """
    
    # load train+dev
    if not ignore_train_dev: data = load_single_dataset(save_path,drop_columns=False)
    else: data = None
    
    # load 4 test sets
    if not ignore_test:
        fpath_t1 = "data/084e02sniff1.csv"          # subject not in training set
        fpath_t2 = "data/088e29sniff1.csv"          # subject not in training set
        fpath_t3 = "data/090e27sniff2.csv"          # subject 1x  in training set
        fpath_t4 = "data/089e72sniff3.csv"          # subject 2x  in training set

        data_t1 = load_single_dataset(fpath_t1,drop_columns=True)
        data_t2 = load_single_dataset(fpath_t2,drop_columns=True)
        data_t3 = load_single_dataset(fpath_t3,drop_columns=True)
        data_t4 = load_single_dataset(fpath_t4,drop_columns=True)
    else: data_t1,data_t2,data_t3,data_t4=None,None,None,None
        
    return data,data_t1,data_t2,data_t3,data_t4


def load_complete_train_dev_plus_tests(NN=1,
                                       load_train_dev=True, 
                                       load_tests=True,
                                       include_fpath=False):
    """ Load data files for train+dev and four tests. """
    
    # make sure one of the two NNs is selected
    assert NN in [1,2],f"Error! NN must be either 1 or 2 and not NN={NN}."

    # initial values in case train+dev or tests are not loaded
    data,data_t1,data_t2,data_t3,data_t4 = None,None,None,None,None
    
    if NN==1:

        # list of datasets for train+dev is combined in a pandas dataFrame
        if load_train_dev:
            # some of the dataset are not used because of memory issues
            fpaths = [
        #    'data/068e21sniff1.csv',
        #    'data/071e31sniff1.csv',
        #    'data/072e17sniff1.csv',
        #    'data/073e02sniff1.csv',
        #    'data/074e02sniff1.csv',
        #    'data/074e46sniff2.csv',
            'data/078e09sniff1.csv',
            'data/079e02sniff1.csv',
            'data/079exxsniff2.csv',
            'data/080e02sniff1.csv',
            'data/082e02sniff1.csv',
            'data/083e02sniff1.csv',
            'data/083e37sniff2.csv',
            'data/085e04sniff1.csv',
            'data/085e08sniff2.csv',
            'data/086e20sniff1.csv',
            'data/086e23sniff2.csv',
            'data/086e34sniff3.csv',
            'data/087e02sniff1.csv',
            'data/087e34sniff2.csv',
            'data/089e39sniff1.csv',
            'data/089e58sniff2.csv',
            'data/090e02sniff1.csv']

            # loop over datasets
            for i,fpath in enumerate(fpaths): 
                # load dataset
                data_temp = pd.read_csv(fpath)

                # drop unnecessary information
                data_temp = data_temp.drop(columns=['bundleID', 'region','threshold','timeStamps','detectionLabel'])

                # remove columns that are of no use for training in particular
                data_temp = data_temp.drop(columns=['channelID', 'clusterID'])

                # add a column to indicate the origin of the data
                if include_fpath: data_temp["DataSetName"] = fpath

                # data stores all data of all datasets
                if i==0: data=data_temp.copy(deep=True)
                else: data = pd.concat([data,data_temp.copy(deep=True)])

            del data_temp


        # load 4 test sets
        if load_tests:
            fpath_t1 = "data/084e02sniff1.csv"          # subject not in training set
            fpath_t2 = "data/088e29sniff1.csv"          # subject not in training set
            fpath_t3 = "data/090e27sniff2.csv"          # subject 1x  in training set
            fpath_t4 = "data/089e72sniff3.csv"          # subject 2x  in training set

            data_t1 = pd.read_csv(fpath_t1)
            data_t2 = pd.read_csv(fpath_t2)
            data_t3 = pd.read_csv(fpath_t3)
            data_t4 = pd.read_csv(fpath_t4)

            data_t1 = data_t1.drop(columns=['bundleID', 'region','threshold','timeStamps','detectionLabel'])
            data_t2 = data_t2.drop(columns=['bundleID', 'region','threshold','timeStamps','detectionLabel'])
            data_t3 = data_t3.drop(columns=['bundleID', 'region','threshold','timeStamps','detectionLabel'])
            data_t4 = data_t4.drop(columns=['bundleID', 'region','threshold','timeStamps','detectionLabel'])
    
    elif NN==2:
        if load_train_dev:
            # load train dev data
            fpath = "./data/density_train_dev.csv"
            data = pd.read_csv(fpath)
        
        if load_tests:
            # load 4 test sets
            fpath_t1 = "data/084e02sniff1_density.csv"          # subject not in training set
            fpath_t2 = "data/088e29sniff1_density.csv"          # subject not in training set
            fpath_t3 = "data/090e27sniff2_density.csv"          # subject 1x  in training set
            fpath_t4 = "data/089e72sniff3_density.csv"          # subject 2x  in training set

            data_t1 = pd.read_csv(fpath_t1)
            data_t2 = pd.read_csv(fpath_t2)
            data_t3 = pd.read_csv(fpath_t3)
            data_t4 = pd.read_csv(fpath_t4)

    
    return data,data_t1,data_t2,data_t3,data_t4
