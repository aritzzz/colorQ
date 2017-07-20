import numpy as np
import closestcentroids

def run(imagem, initial_centroids, max_iters):

    centroids = initial_centroids
    K = centroids.shape[0]

    for i in range(max_iters):

        indexed = closestcentroids.index(centroids, imagem)

        centroids = closestcentroids.computecentroids(imagem,indexed, K)

    return centroids, indexed

