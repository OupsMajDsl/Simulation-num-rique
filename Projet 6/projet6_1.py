import numpy as np
import matplotlib.pyplot as plt

nb_file = 19
lg_file = len(np.loadtxt("Projet 6/PROJET6.1/mes1.dat")[:, 0])
ampl    = np.zeros((nb_file, lg_file))
phas    = np.zeros((nb_file, lg_file))
fig, ax = plt.subplots(2, 3, figsize = (25, 15))

for k_file in range(1, nb_file + 1):
    filename         = "Projet 6/PROJET6.1/mes{}.dat".format(k_file)
    file_load        = np.loadtxt(filename)
    real             = file_load[:, 2]
    imag             = file_load[:, 1]
    ampl[k_file - 1] = np.sqrt(real**2 + imag**2)
    phas[k_file - 1] = np.arctan2(real, imag)
    if k_file == 1:
        fq = file_load[:, 0]

for i in range(len(ampl[:, 0])):
    col = 0                                             #tracé linéaire    
    ax[0, col].plot(fq, ampl[i], alpha = 0.3)
    ax[0, col].set_ylabel('Amplitude linéaire')
    ax[1, col].plot(fq, phas[i], alpha = 0.3)
    ax[1, col].set_ylabel('Phase en radian')

    col = 1                                             #tracé db + phase déroulée
    ampl_db = 20* np.log10(ampl[i])
    ax[0, col].plot(fq, ampl_db)
    ax[0, col].set_ylabel('Amplitude (dB)')
    ax[1, col].plot(fq, np.unwrap(phas[i]))
    ax[1, col].set_ylabel('Phase déroulée en radian')

std_ampl = []                                           #tracé écart-type
std_phas = []
col      = 2
for i in range(lg_file):
    std_ampl.append(np.abs((np.std(ampl[:, i]))/np.mean(ampl[:, i])* 100))
    std_phas.append(np.abs((np.std(phas[:, i]))/np.mean(phas[:, i])* 100))
ax[0, col].plot(fq, std_ampl)
ax[0, col].axis([0, 1000, 0, 30])
ax[0, col].set_ylabel('Amplitude')
ax[1, col].plot(fq, std_phas)
ax[1, col].axis([0, 1000, 0, 100])
ax[0, col].set_ylabel('Phase')

for col in range(3):
    ax[0, col].set_xticklabels([])
    ax[1, col].set_xlabel('Fréquence (Hz)')
    ax[0, col].set_title('Spectre (superposition des {} fichiers)'.format(nb_file))
ax[0, 2].set_title('Ecart-type relatif en %')

plt.tight_layout()
plt.show()