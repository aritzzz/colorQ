import numpy as np


def index(initial_centroids, imagem):   
    K = initial_centroids.shape[0] 
    idx = np.zeros((imagem.shape[0],1)) 

    d = np.zeros((K,1))  #print the shape of d

    for i in range(imagem.shape[0]):
        for j in range(K):
            d[j] = np.sum(((imagem[i,:] - initial_centroids[j,:])**2))
        I = np.argmin(d)
        idx[i] = I


    return idx  #hey listen man, you can as well serialize idx so that this
                #script would run only once

#idx = np.save('savedidx.npy',idx)



    
        
def computecentroids(imagem, idx, K):
    a = imagem.shape
    centroids = np.zeros((K,a[1]))

    for i in range(K):
        p = np.concatenate((idx , imagem), axis = 1)
        #print p.shape
        q = p[p[:,0] == i, 1:]
        #print q.shape
        
        centroids[i,:] = (q.sum(axis = 0))/q.shape[0]
 
    return centroids 
        

    

                         
