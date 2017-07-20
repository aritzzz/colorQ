




import matplotlib.image as img
import numpy as np
import initcentroids
import closestcentroids
import runkmeans

image = img.imread('img.png')
image = np.array(image)
imagem = np.reshape(image, (np.shape(image)[0]*np.shape(image)[1], np.shape(image)[2]))
#imagem = imagem/255  #This was major issue 
 
K = 30
max_iters = 15

initial_centroids = initcentroids.centroids(imagem,K) 

centroids,indexed  = runkmeans.run(imagem,initial_centroids, max_iters)

indexed = closestcentroids.index(centroids, imagem)

recovered_imagem = np.zeros((indexed.shape[0], centroids.shape[1]))




for i in range(indexed.shape[0]):
    recovered_imagem[i,:] = centroids[int(indexed[i]), :]

recovered_image = np.reshape(recovered_imagem, (image.shape[0], image.shape[1], image.shape[2]))

np.save('imagematrix.npy', recovered_image)







