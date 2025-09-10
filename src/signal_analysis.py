import numpy as np
from scipy.signal import butter, filtfilt
import pandas as pd
import matplotlib.pyplot as plt
import os

# -----------------------------
# Core reusable functions
# -----------------------------

def generate_noisy_signal(frequency=5, t=None, noise_std=0.5):
    """Generate a sine wave with added Gaussian noise."""
    if t is None:
        t = np.linspace(0, 1, 500)
    clean = np.sin(2 * np.pi * frequency * t)
    noisy = clean + np.random.normal(0, noise_std, size=clean.shape)
    return t, clean, noisy

def apply_lowpass_filter(signal, cutoff, sampling_rate, order=4):
    """Apply Butterworth low-pass filter to a signal."""
    nyq = 0.5 * sampling_rate
    b, a = butter(order, cutoff / nyq, btype="low")
    filtered = filtfilt(b, a, signal)
    return filtered

def save_signal_metrics(time, clean, noisy, filtered, sampling_rate, results_path="results"):
    """Save plots and metrics (SNR, PSNR) to files."""
    os.makedirs(os.path.join(results_path, "plots"), exist_ok=True)

    # Noisy signal plot
    plt.figure()
    plt.plot(time, noisy)
    plt.title("Noisy Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.savefig(os.path.join(results_path, "plots/noisy_signal.png"))
    plt.close()

    # Filtered signal plot
    plt.figure()
    plt.plot(time, filtered)
    plt.title("Filtered Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.savefig(os.path.join(results_path, "plots/filtered_signal.png"))
    plt.close()

    # FFT spectrum plot
    fft_vals = np.fft.fft(filtered)
    fft_freq = np.fft.fftfreq(len(filtered), 1/sampling_rate)
    plt.figure()
    plt.plot(fft_freq[:len(fft_freq)//2], np.abs(fft_vals)[:len(fft_vals)//2])
    plt.title("FFT Spectrum")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.savefig(os.path.join(results_path, "plots/spectrum.png"))
    plt.close()

    # Compute metrics
    def snr(signal, noise):
        return 10*np.log10(np.sum(signal**2)/np.sum(noise**2))
    def psnr(original, processed):
        mse = ((original-processed)**2).mean()
        return 10*np.log10(np.max(original)**2/mse)

    noisy_snr = snr(clean, noisy-clean)
    filtered_snr = snr(clean, filtered-clean)
    filtered_psnr = psnr(clean, filtered)

    metrics = pd.DataFrame({
        "Metric":["Noisy_SNR","Filtered_SNR","Filtered_PSNR"],
        "Value":[noisy_snr, filtered_snr, filtered_psnr]
    })
    metrics_file = os.path.join(results_path, "metrics_v0_1.csv")
    metrics.to_csv(metrics_file, index=False)

    return metrics_file
