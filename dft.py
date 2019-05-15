import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import math

WAVE_OUTPUT_FILENAME = input('Enter name of audio file you want to use:')
fs,data = wavfile.read(WAVE_OUTPUT_FILENAME)
# frequency = input('Enter the frequency of the periodic wave:')
Time = input('Enter the period of the wave: ')
T = float(Time)

sampling_frequency = int(input('Enter the sampling frequency of the audio: '))
no_of_samples = int(T*sampling_frequency)
fourier_components = np.fft.rfft(data,no_of_samples)
mag = np.abs(fourier_components)
phase = np.angle(fourier_components)

max = np.nanmax(mag)
mag_norm = mag/max
len_four = len(mag)
freqs = np.fft.rfftfreq(no_of_samples,1/sampling_frequency)
plt.figure()
plt.stem(freqs[:len_four//2], mag_norm[:len_four//2], width = 1.5)
plt.show()


w0 = (2*np.pi)/(T)
comps = np.zeros([1,len_four*100], dtype = complex)
t = np.linspace(0,T*50,len_four*100)

plt.figure()
for i in range(len_four):
    harmonic = np.zeros([1,len_four*100], dtype = complex)
    # plt.plot(t,comps[0, :],'r')
    for j in range(len_four*100):
        harmonic[0,j] = harmonic[0,j] + mag_norm[i]*complex(math.cos(t[j]*i*w0 + phase[i]), math.sin(t[j]*i*w0 + phase[i]))
    comps[0,:] = comps[0,:] + harmonic[0, :]
plt.plot(t,comps[0,:],'r')
plt.show()


name_aud = input('Enter the name of audio file: ')
wavfile.write(name_aud, sampling_frequency, comps[0,:].real)



