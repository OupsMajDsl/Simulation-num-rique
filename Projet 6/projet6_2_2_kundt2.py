import numpy as np
import matplotlib.pyplot as plt

freq    = 1000
nb_file = 50
delta_f = 5000/4096
lg_file = len(np.loadtxt("Projet 6/PROJET6.2/kundt2/kundt1.txt")[:, 0])
mod     = []
phas    = []
fq      = np.arange(0, lg_file*delta_f, delta_f)
pos     = [0.01]

def find_nearest(array, value):         #https://stackoverflow.com/questions/2566412/find-nearest-value-in-numpy-array
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx

indice = find_nearest(fq, freq)
        
#[row, col]
for k_file in range(1, nb_file + 1):
    data        = np.loadtxt("Projet 6/PROJET6.2/kundt2/kundt{}.txt".format(k_file))
    if k_file != 1:
        pos.append(((k_file*2)-1)/100)
        
    real        = data[indice, 0]
    imag        = data[indice, 1]
    mod.append(np.sqrt(real**2 + imag**2))
    phas.append(np.arctan2(imag, real))
    
    
#ajustement théorique 
x = pos
f = fq[indice]
c_0 = 344
w   = 2*np.pi*f
k   = w/c_0
phi = 3            #décale la courbe
R   = 1            #augmente l'amplitude
p_th = []
for i in range(nb_file):
    p_th.append(np.abs(np.exp(1j* k* x[i]) + R* np.exp(1j* phi)* np.exp(-1j* k* x[i])))

fig, ax = plt.subplots(2, 1)
ax[0].plot(pos, mod,  'o-', label = 'Mesure')
ax[1].plot(pos, phas, 'o-', label = 'Mesure')

ax[0].plot(pos, p_th, label = 'Théorie')

ax[0].set_title("Pression pour le matériau kundt2 à la fréquence {:.2f} Hz".format(fq[indice]))
ax[0].set_ylabel('Amplitude')
ax[1].set_ylabel('Phase')
ax[1].set_xlabel('Position [m]')
ax[0].set_xticklabels([])
for i in range(len(ax)):
    ax[i].grid()
    ax[i].legend()

plt.show()
