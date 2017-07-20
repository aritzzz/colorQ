




import matplotlib.image as img
import numpy as np
import initcentroids
import closestcentroids
import runkmeans

image = img.imread('img.png')
image = np.array(image)
imagem = np.reshape(image, (np.shape(image)[0]*np.shape(image)[1], np.shape(image)[2]))
imagem = imagem/255
##
K = 16
max_iters = 10
##
initial_centroids = initcentroids.centroids(imagem,K) #to randomly initialize centroids
##
#indexed = closestcentroids.index(initial_centroids, imagem)
##
#centroids  = closestcentroids.computecentroids(imagem, indexed, K)

centroids, indexed = runkmeans.run(imagem,initial_centroids, max_iters)

recovered_imagem = np.zeros((indexed.shape[0], centroids.shape[1]))


for i in range(indexed.shape[0]):
    recovered_imagem[i,:] = centroids[int(indexed[i]), :]

recovered_image = np.reshape(recovered_imagem, (image.shape[0], image.shape[1],3))

np.save('imagematrix', recovered_image)

f.close()






