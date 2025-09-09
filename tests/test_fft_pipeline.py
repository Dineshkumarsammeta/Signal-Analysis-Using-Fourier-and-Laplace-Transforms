import numpy as np
import pandas as pd
from scipy.signal import butter, filtfilt

# Import your main processing function
# from demo.signal_processing import run_fft_pipeline
# For demo purposes, let's inline a simplified version

def run_fft_pipeline(signal, sampling_rate=100, cutoff=2, order=4):
    """Simple FFT + low-pass filter pipeline"""
    # Low-pass filter
    nyq = 0.5 * sampling_rate
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    filtered_signal = filtfilt(b, a, signal)

    # FFT
    fft_vals = np.fft.fft(filtered_signal)
    fft_freq = np.fft.fftfreq(len(filtered_signal), 1/sampling_rate)
    return filtered_signal, fft_vals, fft_freq

def test_fft_smoke():
    """Smoke test: small synthetic signal runs through pipeline"""
    # Tiny synthetic signal
    time = np.linspace(0, 1, 10)
    signal = np.sin(2 * np.pi * 1 * time)  # 1 Hz sine

    filtered_signal, fft_vals, fft_freq = run_fft_pipeline(signal)

    # Checks
    assert len(filtered_signal) == len(signal)
    assert len(fft_vals) == len(signal)
    assert len(fft_freq) == len(signal)
    assert np.isfinite(filtered_signal).all()
    assert np.isfinite(fft_vals).all()
    assert np.isfinite(fft_freq).all()
