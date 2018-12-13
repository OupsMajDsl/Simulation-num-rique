import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

rate, data = wavfile.read('Projet 6/PROJET6.3/gong.wav')
t1 = np.linspace(0, len(data)/rate, len(data))

gnog = data[::-1]
wavfile.write('Projet 6/PROJET6.3/gnog.wav', 44100, gnog)

fig, ax = plt.subplots()
ax.plot(t1, gnog)
ax.grid(True)
plt.show()
# print(data)


rate, data = wavfile.read('Projet 6/PROJET6.3/countdown1.wav')
t2 = np.linspace(0, len(data)/rate, len(data))

countup = data[::-1]
wavfile.write('Projet 6/PROJET6.3/countup1.wav', 44100, countup)

fig, ax = plt.subplots()
ax.plot(t2, countup)
ax.grid(True)
plt.show()