import os
os.environ["CUDA_DEVICE_ORDER"]="PCI_BUS_ID"
os.environ['CUDA_VISIBLE_DEVICES'] = '0,1,2,3'
import keras
import tensorflow as tf
from keras.layers import *
from keras import optimizers
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.utils import np_utils
from keras.layers import Input, Dense, TimeDistributed, Conv2D, Flatten, BatchNormalization
from keras.models import Model
from keras import metrics
import pandas as pd 
from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import custom_loss
import keras.backend as K
from keras.utils import plot_model
from scipy.io import loadmat

def custom_categorical_hinge(y_true, y_pred):
    n = (y_pred.shape[1])
    n = int(n)
    scale = 50
    isMask = np.arange(n,dtype=np.float32)
    isMask = np.exp(isMask/scale)
    isMask = tf.cast(isMask,tf.float32)
    num = K.sum(isMask)
    isMask = tf.div(isMask,num)
    isMask = tf.reshape(isMask,[n,1])
    y_true = tf.matmul(y_true,isMask)
    y_pred = tf.matmul(y_pred,isMask)
    pos = K.sum(y_true * y_pred)
    neg = K.max((1. - y_true) * y_pred)
    tmp = neg-pos+1.
    err = K.maximum(0., tmp)   
    return err

def custom_hinge(y_true, y_pred):
    n = (y_pred.shape[1])
    n = int(n)
    scale = 50
    isMask = np.arange(n,dtype=np.float32)
    isMask = np.exp(isMask/scale)
    isMask = tf.cast(isMask,tf.float32)
    num = K.sum(isMask)
    isMask = tf.div(isMask,num)
    isMask = tf.reshape(isMask,[n,1])
    error = K.maximum(1. - y_true * y_pred, 0.)
    print(error)
    error = tf.matmul(error,isMask)
    return error

def custom_mse(y_true, y_pred):

    #find which values in yTrue (target) are the mask value
    n = (y_pred.shape[1])
    n = int(n)
    scale = 50
    isMask = np.arange(n,dtype=np.float32)
    isMask = np.exp(isMask/scale)    
    num = K.sum(isMask)
    isMask = tf.div(isMask,num)
    isMask = tf.reshape(isMask,[n,1])
    error1 = tf.matmul(K.square(y_pred - y_true),isMask)
    error1 = K.sum(error1,axis=-1)
    return error1
   
    #return keras.losses.mean_squared_error(y_pred, y_true)
    
def custom_categorical_accuracy(y_true, y_pred):
    n = (y_pred.shape[1])
    n = int(n)
    scale = 50
    isMask = np.arange(n,dtype=np.float32)
    isMask = np.exp(isMask/scale)
    isMask = tf.cast(isMask,tf.float32)
    num = K.sum(isMask)
    isMask = tf.div(isMask,num)
    isMask = tf.reshape(isMask,[n,1])
    y_true = tf.matmul(y_true,isMask)
    y_pred = tf.matmul(y_pred,isMask)
    acc = K.cast(K.equal(K.argmax(y_true),
                          K.argmax(y_pred)),
                  K.floatx())
    acc = tf.cast(acc,tf.float32)
    return acc

def custom_crossentropy(y_true, y_pred):
    n = (y_pred.shape[1])
    n = int(n)
    scale = 50
    isMask = np.arange(n,dtype=np.float32)
    isMask = (isMask/scale)
    isMask = tf.cast(isMask,tf.float32)
    num = K.sum(isMask)
    isMask = tf.div(isMask,num)
    isMask = tf.reshape(isMask,[n,1])       
    cost = -(tf.multiply(y_true,tf.log(y_pred))+tf.multiply((1-y_true),tf.log(1-y_pred)))
    cost = tf.matmul(cost,isMask)
    return cost

def custom_accuracy(y_true, y_pred):
    n = (y_pred.shape[1])
    n = int(n)
    scale = 50
    isMask = np.arange(n,dtype=np.float32)
    isMask = (isMask/scale)
    isMask = tf.cast(isMask,tf.float32)
    num = K.sum(isMask)
    isMask = tf.div(isMask,num)
    isMask = tf.reshape(isMask,[n,1])   
    acc = K.equal(y_true, K.round(y_pred))
    acc = K.cast(acc,tf.float32)
    acc = tf.matmul(acc,isMask)
    return acc

def binary_accuracy(y_true, y_pred):
    return K.mean(K.equal(y_true, K.round(y_pred)), axis=-1)
    
def train_model_fc(X,y,f1,f2):
    #build your N models
    keras.backend.clear_session()
    inputs = Input(shape=(X.shape[1],X.shape[2])) 
    
    x = TimeDistributed(Dense(128,activation='sigmoid'))(inputs)
    x = TimeDistributed(Dense(64,activation='sigmoid'))(x)
    x = TimeDistributed(Dense(32,activation='sigmoid'))(x)
    x = TimeDistributed(Dense(16,activation='sigmoid'))(x)
    x = TimeDistributed(Dropout(0.5))(x)
    x = TimeDistributed(Flatten())(x)
    x = LSTM(128, activation='softmax',dropout=0.5)(x) 
    
    output1 = Dense(y.shape[1],activation='sigmoid')(x)
    model = Model(input=inputs, output=[output1])
    sgd = optimizers.SGD(lr=0.00005, decay=1e-6, momentum=0.9, nesterov=True)
    adam = optimizers.Adam(lr=0.00001)
    model.compile(optimizer=adam, loss=custom_crossentropy,metrics=[custom_accuracy])
    history = model.fit(X, y, epochs=100, batch_size=32, validation_split=0.1,shuffle=True)
    model.save_weights("rnn.hdf5")
    model.save('rnn_model.h5')
    print('train end')
    
    yhat1 = model.predict(f1,verbose=0)
    yhat2 = model.predict(f2,verbose=0)
    yhat1 = np.mean(yhat1,axis=0)
    yhat2 = np.mean(yhat2,axis=0)

    n = (yhat1.shape[0])
    yhat1 = np.reshape(yhat1,(1,n))
    yhat2 = np.reshape(yhat2,(1,n))

    n = int(n)
    scale = 50
    isMask = np.arange(n,dtype=np.float32)
    isMask = np.exp(isMask/scale)
    num = np.sum(isMask)
    isMask = np.divide(isMask,num)
    isMask = np.reshape(isMask,[n,1])
    y_pred1 = np.matmul(yhat1,isMask)
    y_pred2 = np.matmul(yhat2,isMask)
    
    return y_pred1,y_pred2
