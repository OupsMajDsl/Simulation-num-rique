import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

rate, data = wavfile.read('Projet 6/PROJET6.3/countdown2.wav')
t1 = np.linspace(0, len(data)/rate, len(data))
#seven --> 2.5s - 4s

def find_nearest(array, value):         #https://stackoverflow.com/questions/2566412/find-nearest-value-in-numpy-array
    array = np.asarray(array)
    idx   = (np.abs(array - value)).argmin()
    return array[idx]

debut = find_nearest(t1, 3.2)
fin   = find_nearest(t1, 3.8)
for i in range(len(t1)):
    if debut == t1[i]:
        i_dbt = i
    if fin == t1[i]:
        i_fin = i

seven = data[i_dbt:i_fin]
wavfile.write('Projet 6/PROJET6.3/seven.wav', 44100, seven)

fig, ax = plt.subplots()
ax.plot(t1[i_dbt:i_fin], seven)
ax.grid(True)
plt.show()