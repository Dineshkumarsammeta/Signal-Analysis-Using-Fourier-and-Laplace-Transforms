# Data Provenance and Sample Policy

## Data Sources

- **PhysioNet MIT-BIH Arrhythmia Database**
  - URL: https://physionet.org/content/mitdb/1.0.0/
  - License: Open access for research and education
  - Usage: ECG signal samples for signal analysis demonstration

## Included Data

- `data/ecg_sample.csv`
  - Small synthetic/excerpted sample of ECG signals
  - Used for demonstration of FFT, filtering, and plotting
  - This is **not patient-identifiable information** and safe for public sharing

## Synthetic Data Policy

- Synthetic signals or excerpts are used to illustrate:
  - Fourier Transform analysis
  - Laplace Transform computations
  - Filter design and noise reduction
- Any reproduction of full datasets must comply with original data licenses
- Public CI tests use **mocked/small samples only**, no sensitive data

## Purpose

This project demonstrates:
- Signal processing techniques in Python
- Handling of time-series biomedical data
- Reproducible plots and computations for CI
