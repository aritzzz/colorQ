import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
im_matrix = np.load('imagematrix.npy')
#print(im_matrix)
imgplot = plt.imshow(im_matrix)
plt.show()
