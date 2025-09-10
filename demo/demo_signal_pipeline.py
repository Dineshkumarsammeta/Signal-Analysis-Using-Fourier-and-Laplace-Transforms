import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.signal_analysis import generate_noisy_signal, apply_lowpass_filter, save_signal_metrics

# Generate signals
time, clean, noisy = generate_noisy_signal()

# Filter noisy signal
filtered = apply_lowpass_filter(noisy, cutoff=2.0, sampling_rate=100)

# Save plots and metrics
metrics_csv = save_signal_metrics(time, clean, noisy, filtered, sampling_rate=100)

print(f"✅ Demo finished. Metrics saved at {metrics_csv}")
