import matplotlib.pyplot as plt
import numpy as np
import math

n = int(input('Enter the number of waves to plot:'))
phase = []
frequency = []
amplitude = []
waves = []
for i in range(n):
    pha_freq = input('Enter the frequency,phase( in degrees) and amplitude,separated by a space:')
    props = pha_freq.split(' ')
    phase.append(float(props[1]))
    frequency.append(float(props[0]))
    amplitude.append(float(props[2]))
    waves.append([])

print(amplitude)
t = np.linspace(0,(1/np.min(frequency))*3,1000)
wave_add = np.zeros([1,len(t)])
for i in range(n):
    for j in range(len(t)):
        waves[i].append(amplitude[i]*math.sin(t[j]*2*np.pi*frequency[i] + math.radians(phase[i])))

    wave_add[0,:] += waves[i]

plt.figure('Adding signals')
for k in range(n):
    plt.plot(t, waves[k], label = str(frequency[k]) + ' Hz ' + 'with phase ' + str(phase[k]))
plt.plot(t,wave_add[0,:], 'r', linewidth = 3, label = 'Superimposed wave')
plt.legend(loc = 'upper right')
plt.show()

