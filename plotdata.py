import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

#import imagem
from script1 import imagem
from script1 import indexed

ax.scatter(imagem[:,0], imagem[:,1], imagem[:,2], s = 1, c = indexed)
plt.show()
