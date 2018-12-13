import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(3, 2, figsize = (20, 5))
plt.subplots_adjust(wspace = 0.4, hspace = 0.4)

theta  = np.linspace(np.pi, 3*np.pi, 1000)
theta4 = np.linspace(1, 3, 1000)
f_4    = np.sin(2* np.pi* theta4)
ax[0, 0].plot(theta, -1* np.sin(-1* theta), 'k')
ax[0, 1].plot(theta, np.sin(2* theta), 'k')

ax[1, 0].plot(theta4, f_4, 'k')
ax[1, 1].plot(theta4, np.abs(f_4), 'k')
ax[2, 0].axvline(x = 1, color = 'k')
ax[2, 0].plot([0, 1], [0, 1], 'k', [1, 2, 3], [0, 0, 0], 'k')
ax[2, 1].axvline(x = 1.5, color = 'k')
ax[2, 1].plot([0.5, 1.5], [0, 1], 'k', [0, 0.5], [0, 0], 'k', [1.5, 2.0], [0, 0], 'k')

for j in range(2):
    for i in range(3):
        ax[i, j].grid(True)
        ax[0, j].set_xticks(np.arange(-np.pi, 5*np.pi, np.pi))
        ax[0, j].set_xticklabels([r"$-\pi$", r"$0$", r"$\pi$", r"$2\pi$", r"$3\pi$", r"$4\pi$"])
        ax[0, j].set_yticks([-1, 0, 1])
        ax[0, j].set_yticklabels([r"$-A$", r"$0$", r"$A$"])
        ax[0, j].axis([-np.pi, 4* np.pi, -1, 1])
        ax[1, j].set_xticks(np.arange(-1, 5, 1))
        ax[2, j].set_xticks(np.arange(0.0, 2.5, 0.5))
        ax[2, j].set_yticklabels([r"$0$", r"$A/2$", r"$A$"])
        ax[2, j].axis([0, 2, 0 , 1])
        
#plots sur plusieurs figures
        ax[1, j].plot([-1, 1], [0, 0], 'k', [3, 4], [0, 0], 'k')
        ax[0, j].plot([-np.pi, np.pi], [0, 0], 'k', [3* np.pi, 4* np.pi], [0, 0], 'k')

#légendes particulières
ax[1, 0].set_yticks([-1, 0, 1])
ax[1, 0].set_yticklabels([r"$-A$", r"$0$", r"$A$"])
ax[1, 0].axis([-1, 4, -1, 1])
ax[1, 1].axis([-1, 4, 0, 1])
ax[1, 1].set_yticks([0, 1])
ax[1, 1].set_yticklabels([r"$0$", r"$A$"])

#numéro figures et ylabel
ax[0, 0].text(11.7, 0.7, '(a)')
ax[0, 0].set_ylabel('$f_1(x)$')
ax[0, 1].text(11.7, 0.7, '(b)')
ax[0, 1].set_ylabel('$f_2(x)$') 
ax[1, 0].text(3.75, 0.6, '(c)')
ax[1, 0].set_ylabel('$f_3(x)$')
ax[1, 1].text(3.75, 0.8, '(d)')
ax[1, 1].set_ylabel('$f_4(x)$')
ax[2, 0].text(1.9, 0.8, '(e)')
ax[2, 0].set_ylabel('$f_5(x)$')
ax[2, 1].text(1.9, 0.8, '(f)') 
ax[2, 1].set_ylabel('$f_6(x)$')

plt.show()