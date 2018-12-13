import numpy as np
import matplotlib.pyplot as plt 

#print("""
#Choisissez un diagramme de directivité dans la liste ci-dessous :
#--------------------------------------
#1 -> omnidirectionnel
#2 -> bidirectionnel
#3 -> cardioide
#4 -> hypercardioide
#5 -> supercardioide
#--------------------------------------""")
#choix = int(input("Indiquez le numéro du diagramme souhaité : "))

for choix in range(1, 6):
    theta = np.linspace(0, 2* np.pi, 180)
    if choix == 1:
        rho  = np.full_like(theta, 1)
        diag = 'omnidirectionnel' 
    elif choix == 2:
        rho  = np.cos(theta)
        diag = 'bidirectionnel'
    elif choix == 3:
        rho  = 1 + np.cos(theta)
        diag = 'cardioïde'
    elif choix == 4:
        rho  = 1 + 2* np.cos(theta)
        diag = 'hypercardioïde'
    elif choix == 5:
        rho  = 1 + 3* np.cos(theta)
        diag = 'supercardioïde'
    rho = np.abs(rho)
    rho = 20* np.log10(rho/max(rho))

    plt.figure()
    ax = plt.subplot(111, polar = True)

    ax.plot(theta, rho)
    ax.set_theta_zero_location('N')
    ax.set_theta_direction('anticlockwise')
    ax.set_xticks(np.arange(0,360,45)/180*np.pi)
    if choix == 1:
        ax.fill_between(theta, np.full_like(theta, -8), rho, color = 'r', alpha = 0.2)
    else:
        ax.fill_between(theta, min(rho), rho, color = 'r', alpha = 0.2)
    ax.grid(True)
    ax.set_ylim(top = 0)
    ax.set_title("Diagramme de directivité de type {}".format(diag))
    plt.show()