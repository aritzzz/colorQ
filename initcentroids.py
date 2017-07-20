import numpy as np
 


initial_centroids = np.zeros((3,1))
def centroids(imagem,K):
    randperm = np.random.permutation(imagem)
    initial_centroids = randperm[ :K, :]
    return initial_centroids
    
    
    
    
