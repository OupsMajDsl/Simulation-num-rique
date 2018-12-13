import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

rate, data = wavfile.read('Projet 6/PROJET6.3/countdown2.wav')
t1 = np.linspace(0, len(data)/rate, len(data))



def find_nearest(array, value):         #https://stackoverflow.com/questions/2566412/find-nearest-value-in-numpy-array
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

#seven --> 2.5 - 4
debut = find_nearest(t1, 3)
fin   = find_nearest(t1, 4)
for i in range(len(t1)):
    if debut == t1[i]:
        i_dbt = i
    if fin == t1[i]:
        i_fin = i

for i in range(len(data)):
        if i < i_dbt:
                data[i] = 0
        if i > i_fin:
                data[i] = 0

print('Done')
wavfile.write('Projet 6/PROJET6.3/riensevenrien.wav', 44100, np.asarray(data))


fig, ax = plt.subplots()
ax.plot(t1, data)
ax.grid(True)
plt.show()