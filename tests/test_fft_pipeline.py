import os
import pandas as pd
import numpy as np
from scipy.signal import butter, filtfilt
from scipy.fft import fft

def test_fft_smoke():
    data_path = os.getenv("DATA_PATH", "data/sample_signal.csv")
    df = pd.read_csv(data_path)
    signal = df["signal"].values

    # Only filter if we have enough samples
    if len(signal) > 20:
        nyq = 0.5 * 100  # assume default sampling rate
        cutoff = 2 / nyq
        b, a = butter(4, cutoff, btype="low", analog=False)
        filtered_signal = filtfilt(b, a, signal)
    else:
        filtered_signal = signal  # too short, skip filtering

    fft_vals = fft(filtered_signal)

    # ✅ Assertions for smoke test
    assert len(fft_vals) == len(filtered_signal)
    assert np.isfinite(fft_vals).all()
