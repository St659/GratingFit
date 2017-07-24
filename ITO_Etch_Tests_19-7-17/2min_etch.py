
import numpy as np
import os
import matplotlib.pyplot as plt

directory= 'E:\\Chrome Download\\19-7-17 2 min Etch\\19-7-17 2 min Etch'
tm_directory = 'E:\\Chrome Download\\19-7-17 2 min Etch\\19-7-17 2 min Etch\\TM'
te_directory = 'E:\\Chrome Download\\19-7-17 2 min Etch\\19-7-17 2 min Etch\\TE'
plt.style.use('seaborn-white')
background_file = os.listdir(directory)
print(background_file)

fig, axes_tm = plt.subplots(2,2)
print(axes_tm)

fig2, axes_te = plt.subplots(2,2)

tm_files = os.listdir(tm_directory)
te_files = os.listdir(te_directory)

flat_tm_axes = [item for sublist in axes_tm for item in sublist]
flat_te_axes = [item for sublist in axes_te for item in sublist]

for file, ax in zip(tm_files, flat_tm_axes):
    wave, reflectance= np.genfromtxt(os.path.join(tm_directory,file), unpack=True, delimiter=',')
    wave, background = np.genfromtxt(os.path.join(directory,background_file[0]), unpack=True, delimiter=',')
    ax.plot(wave, np.divide(reflectance, background), linewidth=0.5)
    ax.set_title(file)
    ax.set_xlabel('Wavelength (nm)')
    ax.set_ylabel('Grating Reflectance/Background reflectance')
    ax.set_xlim([500, 900])
    ax.set_ylim([0.8, 1.5])

for file, ax in zip(te_files, flat_te_axes):
    wave, reflectance= np.genfromtxt(os.path.join(te_directory,file), unpack=True, delimiter=',')
    wave, background = np.genfromtxt(os.path.join(directory,background_file[0]), unpack=True, delimiter=',')
    ax.plot(wave, np.divide(reflectance, background), linewidth=0.5)
    ax.set_title(file)
    ax.set_xlabel('Wavelength (nm)')
    ax.set_ylabel('Grating Reflectance/Background reflectance')
    ax.set_xlim([500, 900])
    ax.set_ylim([0.5, 1.5])


plt.show()

