import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

rate, data = wavfile.read('Projet 6/PROJET6.3/countdown1.wav')
t1 = np.linspace(0, len(data)/rate, len(data))

def find_nearest(array, value):         #https://stackoverflow.com/questions/2566412/find-nearest-value-in-numpy-array
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]
#five --> 5.6 - 6.4
debut = find_nearest(t1, 5.6)
fin   = find_nearest(t1, 6.4)
for i in range(len(t1)):
    if debut == t1[i]:
        i_dbt = i
    if fin == t1[i]:
        i_fin = i

five = []
dat = data[i_dbt:i_fin]
for i in range(5):
    for j in range(len(dat)):
        five.append(dat[j])

print('Done')
print(len(five))
print(len(dat))
wavfile.write('Projet 6/PROJET6.3/fivefive.wav', 44100, np.asarray(five))

t_five = np.linspace(0, len(five)/rate, len(five))

fig, ax = plt.subplots()
ax.plot(t_five, five)
ax.grid(True)
plt.show()