# Audio Noise Cancellation with FFT in Python

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

This project demonstrates a fundamental digital signal processing (DSP) technique by generating a clean audio signal, corrupting it with synthetic noise, and implementing a filter to remove the noise using the **Fast Fourier Transform (FFT)**.

The entire process—from the original clean signal to the noisy version and the final filtered output—is visualized and played back as audio, providing clear, tangible results.

---

## Visual Demonstration

The effectiveness of the noise cancellation filter is clearly demonstrated in both the frequency and time domains.

### Frequency Domain Analysis (The Core Logic)
The plot below shows the signal's spectrum at each stage. The middle plot clearly shows two large spikes representing the synthetic noise, which are completely removed in the bottom plot after filtering.

![Frequency Analysis Plots]((https://github.com/Mo-Shams/Signal-processing/blob/main/Frequency%20domain%20plots.jpeg))

### Time Domain Waveform
This plot shows the signal's amplitude over time. While the effect of the noise is less obvious to the eye here, the middle plot shows a much more dense and erratic waveform compared to the cleaner, more structured original and filtered signals.

![Time Domain Plots]((https://github.com/Mo-Shams/Signal-processing/blob/main/Time%20domain%20plots.jpeg))

---

## Key Features

- **Audio Signal Generation:** Creates a multi-tone audio signal by combining sine waves of specific musical notes.
- **Frequency Domain Analysis:** Transforms the signal from the time domain to the frequency domain using SciPy's FFT to analyze its spectral components.
- **Noise Identification & Filtering:** Intelligently identifies the most dominant frequency spikes (assumed to be noise) and nullifies them.
- **Signal Reconstruction:** Reconstructs the clean audio signal from the filtered frequency spectrum.
- **Real-time Visualization:** Uses Matplotlib to plot the original, noisy, and filtered signals in both the time and frequency domains for clear comparison.

---

## Tech Stack

- **Language:** **Python**
- **Libraries:**
    - **NumPy:** For numerical operations and signal array manipulation.
    - **SciPy:** For implementing the Fast Fourier Transform (`fft`).
    - **Matplotlib:** For data visualization and plotting the signal waveforms.
    - **Sounddevice:** For real-time audio playback.

---
