import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.fft import fft

# Set up a time variable over 3 seconds where the wave is sampled 44100 per second
t = np.linspace(0, 3, 3 * 44100)

# Defining number of note pairs
N = 4

# Defining Frequencies of each note pairs from the Octaves table 
F = np.array([130.81, 146.83, 164.81, 174.61])  #C3, D3, E3, F3 
f = np.array([261.63, 293.66, 329.63 , 349.23]) #C4, D4, E4, F4

# Defing start period and duration period
t_array = np.array([0.0, 0.75, 1.5, 2.25])   #Start time of each note pair in seconds
T_array = np.array([0.75, 0.75, 0.75 ,0.75]) #Duration of each note pair in seconds

# Initializing signal
x = np.zeros(t.shape, dtype = t.dtype)

# Building the signal by summation
for i in range(N):
    # Variable representing the subtraction of the unit Impulses (u(t - ti) - u(t - ti - Ti))
    unitStepFactor = np.logical_and(t >= t_array[i] , t <= (t_array[i] + T_array[i]))
    # Using the Series Formula
    x += (np.sin(2 * np.pi * F[i] * t) + np.sin(2 * np.pi * f[i] * t)) * unitStepFactor

# Sets the number of samples to 3 * 44100 and the frequency axis range
N_samples = 44100 * 3
freqs = np.linspace(0, 44100/2, N_samples//2, endpoint = False)

# Converts the Generated Signal without noise from the time domain to the Frequency domain.
x_f = fft(x)
x_f = 2 / N_samples * np.abs(x_f[:N_samples//2])

# Randomly selects 2 Integer frequencies between 0 and 512 to be the noise frequencies.
fn1, fn2 = np.random.randint(0, 512, 2)

# Generates noise Signals.
n_t = np.sin(2* np.pi * fn1 * t) + np.sin(2 * np.pi * fn2 * t)

# Generating Song with noise added in Time and Fequency domain. 
x_n = x + n_t
x_n_f = fft(x_n)
x_n_f = 2 / N_samples * np.abs(x_n_f[:N_samples//2])

# a function the returns the position of the max element in a list.
def get_max(a):
    max_reached = 0
    idx = -1
    for i in range (len(a)):
        if(a[i] > max_reached):
            max_reached = a[i]
            idx = i
    return idx

# Intializing Signal for noise cancelation in Frequency domain.
x_n_f_removed = x_n_f + 0
# Finding position of the first maximum frequency in Signal with noise.
idx_mx_1 = get_max(x_n_f_removed)
# Setting that frequency in the Signal with 0.
x_n_f_removed[idx_mx_1] = 0
# Saving the first Frequency that was removed.
freq_1 = freqs[idx_mx_1]
# Finding position of the second maximum Frequency in Signal with noise.
idx_mx_2 = get_max(x_n_f_removed)
# Saving the second Frequency that was removed.
freq_2 = freqs[idx_mx_2]
# Setting that frequency in the Signal with 0.
x_n_f_removed[idx_mx_2] = 0

# Removing the noise signals from the song signal in Time domain. 
x_n_removed = x_n - np.sin(2 * np.pi * freq_1 * t) - np.sin(2 * np.pi * freq_2 * t)


# Ploting Signals in Time Domain.
plt.figure(figsize=(18, 16))

# Ploting Generated Signal without noise in Time Domain. 
plt.subplot(3,1,1)
plt.plot(t, x) # [t<0.1] makes the samples cleaner
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Generated Signal Without Any Noise Added Yet')
plt.ylim([-2, 2])
plt.xlim(0, 3)

# Plays the Song without noise added.
sd.play(x, 44100) # multiplying by 3 makes it play in 1 second.
sd.wait()

#Plotting Generated Signal with Noise in Time Domain.
plt.subplot(3,1,2) 
plt.plot(t, x_n)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Generated Signal With Noise Added')
plt.ylim([-2, 2])
plt.xlim(0, 3)

# Plays the Song with noise added.
sd.play(x_n, 44100)
sd.wait()


#Plotting Generated Signal after Noise Cancelation in Time Domain.
plt.subplot(3,1,3)
plt.plot(t,x_n_removed)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Generated Signal After Undergoing Noise Cancelation')
plt.ylim([-2, 2])
plt.xlim(0, 3)

# Plays the Song after undergoing noise cancellation.
sd.play(x_n_removed, 44100)
sd.wait()


# Plot Signals in Frequency domain
plt.figure(figsize=(18, 16))

# Ploting Generated Signal without noise in Frequency Domain.
plt.subplot(3,1,1)
plt.plot(freqs, x_f)
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude')
plt.title('Generated Signal Without Any Noise Added Yet')
plt.xlim(0, 512)

#Plotting Generated Signal with Noise in Frequency Domain.
plt.subplot(3,1,2)
plt.plot(freqs, x_n_f)
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude')
plt.title('Generated Signal With Noise Added')
plt.xlim(0, 512)

#Plotting Generated Signal after Noise Cancelation in Frequency Domain.
plt.subplot(3,1,3)
plt.plot(freqs, x_n_f_removed)
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude')
plt.title('Generated Signal After Undergoing Noise Cancelation')
plt.xlim(0, 512)

# Showing All the Plots.
plt.show()


