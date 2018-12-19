import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

fig, ax = plt.subplots()
plt.subplots_adjust(top = 0.65)
t       = np.arange(0.0, 1.0, 0.001)
a0      = 5
f0      = 3
p0      = 1
s       = a0* np.sin(2* np.pi* f0* t + p0)
ligne,  = plt.plot(t, s, lw = 2, color='red')
ax.set_title('Sinus: $f = {:.2f} Hz$, $A = {:.2f} Pa$, $\Phi = {:.2f} rad$'.format(f0, a0, p0))
ax.axis([0, 1, -10, 10])

axfreq  = plt.axes([0.15, 0.85, 0.75, 0.05], facecolor = 'beige')
sfreq   = Slider(axfreq, 'Fréquence', 0.1, 30.0, valinit = f0)
axamp   = plt.axes([0.15, 0.80, 0.75, 0.05], facecolor = 'beige')
samp    = Slider(axamp, 'Amplitude', 0.1, 30.0, valinit = a0)
axphase = plt.axes([0.15, 0.75, 0.75, 0.05], facecolor = 'beige')
sphase  = Slider(axphase, 'Phase', 0.1, 30.0, valinit = p0)

def miseAjour(val):
    freq  = sfreq.val 
    amp   = samp.val
    phase = sphase.val
    ligne.set_ydata(amp* np.sin(2* np.pi* freq* t + phase))
    ax.set_title('Sinus: $f = {:.2f} Hz$, $A = {:.2f} Pa$, $\phi = {:.2f} rad$'.format(freq, amp, phase)) 
sfreq.on_changed(miseAjour)
samp.on_changed(miseAjour)
sphase.on_changed(miseAjour)

resetax = plt.axes([0.05, 0.93, 0.20, 0.04])
bouton = Button(resetax, 'Remise à zéro', color = 'red', hovercolor = 'lightblue')
def miseAzero(event):
    sfreq.reset()
    samp.reset()
    sphase.reset()
bouton.on_clicked(miseAzero)

plt.show()