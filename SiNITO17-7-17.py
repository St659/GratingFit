import numpy as np
import os
import matplotlib.pyplot as plt

def plot_graphs(fig, ax, ax2, wave, reflectance, background):
    ax.plot(wave, reflectance, linewidth= 0.5)
    ax.plot(wave, background, linewidth= 0.5)
    ax2.plot(wave, np.divide(reflectance, background), linewidth= 0.5)
    ax.set_ylabel('Reflectance')
    ax.set_xlabel('Wavelength (nm)')
    ax2.set_xlabel('Wavelength (nm)')
    ax2.set_ylabel('Grating Reflectance/Background reflectance')
    ax2.set_xlim([500, 900])
    ax2.set_ylim([0.8, 1.5])

directory= 'E:\\Chrome Download\\ITO SiN images\\ITO SiN images'
plt.style.use('seaborn-white')
files = os.listdir(directory)
print(files)


ito_325 = os.path.join(directory,files[4])
ito_325_background = os.path.join(directory, files[1])

ito_315 = os.path.join(directory,files[3])
ito_315_background = os.path.join(directory, files[2])

wave, reflectance_325= np.genfromtxt(ito_325, unpack=True, delimiter=',')
wave, background_325 = np.genfromtxt(ito_325_background, unpack=True, delimiter=',')

wave, reflectance_315= np.genfromtxt(ito_315, unpack=True, delimiter=',')
wave, background_315 = np.genfromtxt(ito_315_background, unpack=True, delimiter=',')
print(wave)

fig, (ax,ax2) = plt.subplots(1,2)

fig2, (ax3, ax4) = plt.subplots(1,2)

plot_graphs(fig, ax, ax2, wave, reflectance_325, background_325)
plot_graphs(fig2, ax3, ax4, wave, reflectance_315, background_315)


plt.show()