from src.signal_analysis import generate_noisy_signal, apply_lowpass_filter, save_signal_metrics

time, clean, noisy = generate_noisy_signal()
filtered = apply_lowpass_filter(noisy, cutoff=2.0, sampling_rate=100)
metrics_csv = save_signal_metrics(time, clean, noisy, filtered, sampling_rate=100)
