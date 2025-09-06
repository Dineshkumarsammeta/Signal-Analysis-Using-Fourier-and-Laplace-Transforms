import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt
import sympy as sp
import pandas as pd
import os

t, s, w = sp.symbols('t s w', real=True, positive=True)

def symbolic_transforms(expr_str):
    """Compute symbolic Laplace and Fourier transforms using SymPy"""
    try:
        expr = sp.sympify(expr_str)
        laplace_expr = sp.laplace_transform(expr, t, s, noconds=True)
        fourier_expr = sp.fourier_transform(expr, t, w)
        return str(laplace_expr), str(fourier_expr)
    except Exception as e:
        return f"Error: {e}", f"Error: {e}"


def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a


def process_signal(signal_type="synthetic", results_dir="static/results"):
    """Generate noisy signal, apply FFT & filtering, save plots."""
    fs = 500  # sampling frequency
    t = np.linspace(0, 1.0, fs)
    results = {}

    if signal_type == "synthetic":
        # Create noisy signal
        clean = np.sin(2 * np.pi * 5 * t)  # 5 Hz sine wave
        noise = 0.5 * np.random.randn(len(t))
        signal = clean + noise

    elif signal_type == "noisy_ecg":
        # Load ECG sample if available
        try:
            data = pd.read_csv("data/ecg_sample.csv")
            signal = data.values.flatten()[:fs]
        except:
            # fallback synthetic ECG-like signal
            signal = np.sin(2 * np.pi * 1 * t) + 0.2 * np.random.randn(len(t))

    else:
        return {}

    # FFT
    spectrum = np.fft.fft(signal)
    freqs = np.fft.fftfreq(len(signal), 1/fs)

    # Low-pass filter
    cutoff = 30.0  # Hz
    b, a = butter_lowpass(cutoff, fs)
    filtered = filtfilt(b, a, signal)

    # Plot noisy signal
    noisy_path = os.path.join(results_dir, "noisy_signal.png")
    plt.figure()
    plt.plot(t, signal)
    plt.title("Noisy Signal")
    plt.savefig(noisy_path)
    plt.close()
    results["noisy_signal"] = noisy_path

    # Plot spectrum
    spec_path = os.path.join(results_dir, "spectrum.png")
    plt.figure()
    plt.plot(freqs[:len(freqs)//2], np.abs(spectrum)[:len(freqs)//2])
    plt.title("Frequency Spectrum (FFT)")
    plt.savefig(spec_path)
    plt.close()
    results["spectrum"] = spec_path

    # Plot filtered signal
    filt_path = os.path.join(results_dir, "filtered_signal.png")
    plt.figure()
    plt.plot(t, filtered, label="Filtered")
    plt.title("Filtered Signal (Butterworth)")
    plt.savefig(filt_path)
    plt.close()
    results["filtered_signal"] = filt_path

    return results
