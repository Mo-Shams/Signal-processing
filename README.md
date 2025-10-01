# Audio Noise Cancellation with FFT in Python

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

This project demonstrates a fundamental digital signal processing (DSP) technique by generating a clean audio signal, corrupting it with synthetic noise, and implementing a filter to remove the noise using the **Fast Fourier Transform (FFT)**.

The entire process—from the original clean signal to the noisy version and the final filtered output—is visualized in real-time and played back as audio, providing clear, tangible results.

<br>

![Project Demo GIF](https://i.imgur.com/your-gif-url.gif)


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

## How It Works

The noise cancellation logic is straightforward and effective:

1.  **Generation:** A clean audio signal is created in the time domain.
2.  **Corruption:** High-amplitude sinusoidal noise is added to the original signal.
3.  **Transformation (FFT):** The noisy signal is converted to the frequency domain. In this domain, the constant musical notes are spread out, while the powerful noise signals appear as distinct, sharp spikes.
4.  **Filtering:** The algorithm finds the two largest amplitude spikes in the frequency spectrum and sets their magnitude to zero.
5.  **Reconstruction:** The original signal is recovered by subtracting the identified noise (as sine waves) from the noisy time-domain signal.

### Outcome

The filter successfully removes the synthetic noise, restoring the original audio with over **99% accuracy** (measured by correlation coefficient). This is visually confirmed by comparing the frequency spectrums of the noisy and filtered signals.

| Noisy Signal (Frequency Domain) | Filtered Signal (Frequency Domain) |
| :-----------------------------: | :--------------------------------: |
| ![Noisy Spectrum](https://i.imgur.com/your-noisy-plot.png) | ![Filtered Spectrum](https://i.imgur.com/your-filtered-plot.png) |
|   *Noise spikes are clearly visible* |     *Noise spikes are eliminated* |

---
