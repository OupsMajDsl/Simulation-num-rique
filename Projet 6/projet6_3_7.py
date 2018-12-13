import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile


rate, data = wavfile.read('Projet 6/PROJET6.3/countdown1.wav')
np.save('Projet 6/PROJET6.3/countdown1.npy', data)
np.savetxt('Projet 6/PROJET6.3/countdown1.txt', data)

#wav --> on peut l'écouter 
#npy, ni lisible, ni écoutable, mais léger sur le HDD
#txt --> on peut voir l'allure du signal, le tracer simplement, mais plus lourd que les autres types de fichiers