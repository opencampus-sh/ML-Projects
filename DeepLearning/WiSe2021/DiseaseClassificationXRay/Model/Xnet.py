from keras.models import Model
from keras.models import Sequential
from keras.layers import Input, Dense, Dropout, Flatten, Conv2D, MaxPool2D, BatchNormalization, Activation, concatenate
from keras.applications import densenet


class Xnet:
    def __init__(self, model2load='custom', percent2retrain=1/6, image_dimensions=(128,128,3), n_classes=14):
        
        self.input_dim  = image_dimensions
        self.n_classes  = n_classes
        self.model      = self.select_model(model2load, percent2retrain)

    # Choose The model ( Custom | Densenet 121(Percent to train(0-1) ))
    def select_model(self, model2load, percent2retrain):
        'Selects the desired model to be loaded'
        if 0>percent2retrain>1:
            raise Exception('Invalid train percentage chosen! Value must be between 0-1')
        elif model2load == 'custom':
            return self.cnn()
        elif model2load == 'densenet121':
            return self.dense_net121(percent2retrain)
        else:
            raise Exception ('Enter valid model name')

    def dense_net121(self, percent2retrain):
        'Returns a Densenet121 architecture NN'
        dense_model = densenet.DenseNet121(input_shape=self.input_dim,
                                             weights='imagenet',
                                             include_top=False)
        # freeze base layers
        if percent2retrain < 1:
            for layer in dense_model.layers[:-int(len(dense_model.layers)*percent2retrain)]: layer.trainable = False

        # add classification top layer
        model = Sequential()
        model.add(dense_model)
        model.add(Flatten())
        model.add(Dense(512, activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(self.n_classes, activation='sigmoid'))
        return model

    def cnn(self):
        'Creates the keras model for binary output'
        # if smaller image_dimensions are used, reduce the number of pooling layers
        model = Sequential()

        model.add(Conv2D(filters=32, kernel_size=(3, 3), padding='Same', activation='relu', input_shape=self.input_dim))
        model.add(Conv2D(filters=32, kernel_size=(3, 3), padding='Same'))
        model.add(Conv2D(filters=32, kernel_size=(3, 3), padding='Same'))
        model.add(BatchNormalization())
        model.add(Dropout(0.1))
        model.add(MaxPool2D(pool_size=(2, 2)))

        model.add(Conv2D(filters=64, kernel_size=(3, 3), padding='Same', activation='relu'))
        model.add(Conv2D(filters=64, kernel_size=(3, 3), padding='Same', activation='relu'))
        model.add(BatchNormalization())
        model.add(Dropout(0.1))
        model.add(MaxPool2D(pool_size=(2, 2)))

        model.add(Conv2D(filters=64, kernel_size=(3, 3), padding='Same', activation='relu'))
        model.add(Conv2D(filters=64, kernel_size=(3, 3), padding='Same', activation='relu'))
        model.add(BatchNormalization())
        model.add(Dropout(0.1))
        model.add(MaxPool2D(pool_size=(2, 2)))

        model.add(Conv2D(filters=128, kernel_size=(3, 3), padding='Same', activation='relu'))
        model.add(Conv2D(filters=128, kernel_size=(3, 3), padding='Same', activation='relu'))
        model.add(BatchNormalization())
        model.add(Dropout(0.1))
        model.add(MaxPool2D(pool_size=(2, 2)))

        model.add(Conv2D(filters=128, kernel_size=(3, 3), padding='Same', activation='relu'))
        model.add(Conv2D(filters=128, kernel_size=(3, 3), padding='Same', activation='relu'))
        model.add(BatchNormalization())
        model.add(Dropout(0.1))
        model.add(MaxPool2D(pool_size=(2, 2)))

        model.add(Conv2D(filters=256, kernel_size=(3, 3), padding='Same', activation='relu'))
        model.add(BatchNormalization())
        model.add(Dropout(0.1))
        model.add(MaxPool2D(pool_size=(2, 2)))

        model.add(Conv2D(filters=256, kernel_size=(3, 3), padding='Same', activation='relu'))
        model.add(BatchNormalization())
        model.add(Dropout(0.1))
        model.add(MaxPool2D(pool_size=(2, 2)))

        #dense block with activation function
        model.add(Flatten())
        model.add(Dense(128, activation="relu"))
        model.add(Dropout(0.5))
        model.add(Dense(self.n_classes, activation="sigmoid"))
        return model


    def get_model(self):
        'Returns the created model'
        return self.model