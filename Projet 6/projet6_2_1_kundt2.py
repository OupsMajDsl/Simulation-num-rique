import numpy as np
import matplotlib.pyplot as plt

dist_data  = [11, 61]
delta_f    = 5000/4096
lg_file    = len(np.loadtxt("Projet 6/PROJET6.2/kundt2/kundt1.txt")[:, 0])
data       = np.zeros((2, lg_file))
fq         = np.arange(0, lg_file*delta_f, delta_f)


for i in range(2):
    file = np.loadtxt("Projet 6/PROJET6.2/kundt2/kundt{}.txt".format( str(int((dist_data[i]/2)+1)) ))
    real = file[:, 0]
    imag = file[:, 1]
    data[i] = np.sqrt(real**2 + imag**2)


fig, ax = plt.subplots(3, 1)
ax[0].plot(fq, 20* np.log10(data[0]), label = r' Pression à {} cm du matériau'.format(dist_data[0]))
ax[0].plot(fq, 20* np.log10(data[1]), label = r'Pression à {} cm du matériau'.format(dist_data[1]))
ax[0].set_xticklabels([])
ax[0].set_title("kundt2")
ax[0].legend()

ax[1].plot(fq, 20*np.log10(data[1]/data[0]))
ax[1].set_xticklabels([])
ax[1].set_title("Réponse en fréquence p{}/p{}".format(dist_data[1], dist_data[0]))

ax[2].plot(fq, 20*np.log10(data[0]/data[1]))
ax[2].set_title("Réponse en fréquence p{}/p{}".format(dist_data[0], dist_data[1]))

for i in range(3):
    ax[i].grid()
plt.show()
