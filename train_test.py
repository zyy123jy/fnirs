F1 = data['F1_1'] # positive 
F2 = data['F2_1'] # negative
F1 = np.array(F1)
F2 = np.array(F2)
idx1 = np.arange(F1.shape[0])
idx1 = np.delete(idx1,i,axis = 0)
idx2 = np.arange(F2.shape[0])
idx2 = np.delete(idx2,i,axis = 0)
F1 = F1[idx1,:,:,:]
F2 = F2[idx2,:,:,:]
    
print(F1.shape[0],F2.shape[0])
    
F1 = np.reshape(F1,(F1.shape[0],F1.shape[1],F1.shape[2],20,20))   
F2 = np.reshape(F2,(F2.shape[0],F2.shape[1],F2.shape[2],20,20))

y1 = np.ones((F1.shape[0],F1.shape[1],F1.shape[2],1),dtype = np.float32)
y2 = np.zeros((F2.shape[0],F2.shape[1],F2.shape[2],1),dtype = np.float32)

F1 = np.reshape(F1,(F1.shape[0]*F1.shape[1],F1.shape[2],F1.shape[3],F1.shape[4]))   
F2 = np.reshape(F2,(F2.shape[0]*F2.shape[1],F2.shape[2],F2.shape[3],F2.shape[4]))

y1 = np.reshape(y1,(y1.shape[0]*y1.shape[1],y1.shape[2]))
y2 = np.reshape(y2,(y2.shape[0]*y2.shape[1],y2.shape[2]))

y = np.concatenate((y1,y2),axis=0)
X = np.concatenate((F1,F2),axis=0)
print(X.shape[0],X.shape[1],X.shape[2],X.shape[3])
    
f1 = data['F1_1']# positive sample
f2 = data['F2_1']# negative sample
f1 = f1[i:i+1,:,:,:]
f2 = f2[i:i+1,:,:,:]
print(f1.shape[0],f1.shape[1],f1.shape[2],f1.shape[3])
f1 = np.reshape(f1,(f1.shape[0]*f1.shape[1],f1.shape[2],20,20))   
f2 = np.reshape(f2,(f2.shape[0]*f2.shape[1],f2.shape[2],20,20))
    
yhat1,yhat2 = train_model(X,y,f1,f2)
print("predicted impaired probability for testing data f1 and f2!")    
print(yhat1,yhat2)
