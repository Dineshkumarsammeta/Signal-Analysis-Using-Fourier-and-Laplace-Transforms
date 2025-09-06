import numpy as np
from src.signal_analysis import apply_lowpass_filter, compute_fft

def test_fft_peak_frequency():
    # Create a simple sine wave
    fs = 100  # Sampling rate
    t = np.linspace(0, 1, fs, endpoint=False)
    freq = 5  # Hz
    signal = np.sin(2 * np.pi * freq * t)
    freqs, spectrum = compute_fft(signal, fs)
    
    peak = freqs[np.argmax(np.abs(spectrum))]
    assert round(peak) == freq

def test_lowpass_filter_removes_high_freq():
    fs = 100
    t = np.linspace(0, 1, fs, endpoint=False)
    signal = np.sin(2 * np.pi * 30 * t)  # 30 Hz signal
    filtered = apply_lowpass_filter(signal, cutoff=10, fs=fs)
    
    # The output should have lower power for high frequency components
    assert np.std(filtered) < np.std(signal)
