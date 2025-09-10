# demo/demo_signal_pipeline.py
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt
from dotenv import load_dotenv

# Load config
load_dotenv(dotenv_path=".env")

SAMPLING_RATE = int(os.getenv("SAMPLING_RATE", 100))
DATA_PATH = os.getenv("DATA_PATH", "data/sample_signal.csv")
RESULTS_PATH = os.getenv("RESULTS_PATH", "results")
PLOTS_PATH = os.path.join(RESULTS_PATH, "plots")
LOWPASS_CUTOFF = float(os.getenv("LOWPASS_CUTOFF", 2.0))
FILTER_ORDER = int(os.getenv("FILTER_ORDER", 4))  # ✅ FIX: now defined

os.makedirs(PLOTS_PATH, exist_ok=True)

# Load data
df = pd.read_csv(DATA_PATH)
time = df["time"].values
signal = df["signal"].values

# Add noise
noisy_signal = signal + np.random.normal(0, 0.1, size=signal.shape)

# Adjust filter order if signal is too short
FILTER_ORDER = min(FILTER_ORDER, max(1, len(signal) // 3))

# Apply low-pass filter
if len(signal) > FILTER_ORDER * 2:
    nyq = 0.5 * SAMPLING_RATE
    cutoff = LOWPASS_CUTOFF / nyq
    b, a = butter(FILTER_ORDER, cutoff, btype="low", analog=False)
    filtered_signal = filtfilt(b, a, noisy_signal)
else:
    filtered_signal = noisy_signal

# Save plots
plt.figure(figsize=(8, 4))
plt.plot(time, noisy_signal, label="Noisy Signal")
plt.plot(time, filtered_signal, label="Filtered Signal", color="green")
plt.legend()
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Demo Signal Processing")
plt.tight_layout()
plt.savefig(os.path.join(PLOTS_PATH, "demo_pipeline.png"))
plt.close()

print("✅ Demo pipeline finished. Plots saved in results/plots/")
