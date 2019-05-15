inputs = Input(shape=(X.shape[1],X.shape[2])) 
    
    x = TimeDistributed(Dense(128,activation='softmax'))(inputs)
    x = TimeDistributed(Dense(64,activation='softmax'))(x)
    x = TimeDistributed(Dense(32,activation='softmax'))(x)
    x = TimeDistributed(Dense(16,activation='softmax'))(x)
    x = TimeDistributed(Dropout(0.5))(x)
    x = TimeDistributed(Flatten())(x)
    x = LSTM(128, activation='softmax',dropout=0.5)(x) 
    
    output1 = Dense(y.shape[1],activation='sigmoid')(x)
    model = Model(input=inputs, output=[output1])
    sgd = optimizers.SGD(lr=0.00005, decay=1e-6, momentum=0.9, nesterov=True)
    adam = optimizers.Adam(lr=0.00001)
    model.compile(optimizer=adam, loss=custom_crossentropy,metrics=[custom_accuracy])
    history = model.fit(X, y, epochs=50, batch_size=32, validation_split=0.1,shuffle=True)
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
