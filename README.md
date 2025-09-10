

# 🧠 Signal Analysis Using Fourier and Laplace Transforms  

## 📌 Overview  
This project demonstrates **signal processing techniques** using **Fourier and Laplace transforms** in Python.  
The focus is on **noise reduction, filtering, and frequency-domain analysis**, with applications in **biomedical signal processing** (e.g., ECG/EEG denoising).  

## 📅 Project Timeline

- **Duration:** Feb 2011 – Mar 2011 

- **Acadamic Year** Second Year - Electrical and Electronics Engineering
  
- **Location:** VIT University, Vellore, India  

## ⚠️ Disclaimer

This project was originally developed and tested in **2011**.  
At that time, it ran successfully in the available Python libraries and environments.  

Due to advancements and changes in library versions (e.g., `numpy`, `scipy`, `matplotlib`, etc.),  
some parts of the code may not run exactly as intended in modern environments without modifications.  

I have kept this repository public to **showcase my problem-solving, algorithmic approach, and project experience** to potential recruiters, particularly in the UK.  
Please note that the focus here is on the **concepts and implementation methods**, rather than up-to-date compatibility.

**Modules Used:** 


| **Module**                                               | **Application in Project**                                                                                                |
| -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **DC Machines and Transformers**                         | Understanding signal distortions due to electrical machines and noise sources in real-world biomedical systems.           |
| **Electromagnetic Field Theory**                         | Basis of wave propagation and interaction of signals with fields, essential for understanding ECG/EEG signal acquisition. |
| **Complex Variables and Partial Differential Equations** | Mathematical foundation for Fourier and Laplace transforms, system modeling, and filter design.                           |
| **Environmental Studies**                                | Consideration of sustainable biomedical applications and ethical handling of patient data.                                |
| **Data Structures and Algorithms**                       | Efficient implementation of FFT, filtering algorithms, and data handling in Python.                                       |

---
Data Source:
PhysioNet (MIT-BIH Arrhythmia Database)

Source: https://physionet.org/content/mitdb/1.0.0/

## ⚙️ Features  
- Generate and visualize **synthetic noisy signals**  
- Apply **Fast Fourier Transform (FFT)** for frequency analysis  
- Design and implement **Butterworth low-pass filters** for noise removal  
- Compute **Laplace transforms** using symbolic math  
- Visualize **time-domain and frequency-domain signals** before and after filtering  

---

## 📂 Project Structure
Signal-Analysis-Fourier-Laplace/
│── data/
│ └── ecg_sample.csv # (optional ECG data)
│── src/
│ └── signal_analysis.py # main Python script
│── results/
│ ├── noisy_signal.png
│ ├── spectrum.png
│ ├── filtered_signal.png
│── README.md


---

## 🚀 Getting Started  

### 🔧 Requirements  
- Python 3.8+  
- NumPy  
- Matplotlib  
- SciPy  
- SymPy  

Install dependencies:  
pip install numpy matplotlib scipy sympy

📊 Results
Noisy Signal (Time Domain)

Frequency Spectrum (FFT)

Filtered Signal (After Low-Pass Filter)

Skills Demonstrated

Digital Signal Processing (DSP)

Fourier Analysis & Filtering

Laplace Transforms (System Modeling)

Python (NumPy, SciPy, SymPy, Matplotlib)

---
## 📊 Signal Denoising — Before vs After

**Noisy Signal (input data)**  
![Noisy Signal](results/plots/noisy_signal.png)

**Filtered Signal (after low-pass filter)**  
![Filtered Signal](results/plots/filtered_signal.png)

**Frequency Spectrum (FFT analysis)**  
![Spectrum](results/plots/spectrum.png)

## 📊 Repository Health

This project is under continuous improvement. An [Audit report](docs/repo_audit.md) has been created to track repository health and enhancements.

### Key Focus Areas
- **Releases & Versioning:** To be added — future releases will follow semantic versioning for clarity and reproducibility.  
- **Expanded Test Coverage:** Planned integration with `pytest` to validate FFT, filtering, and Laplace transform outputs.  
- **Metrics / Artifacts Integration:** Export of CSV and PNG results in CI workflows to ensure reproducibility and easy visualization of outputs.


### 🔧 contact 
For questions, collaboration, or feedback, please contact:  
**Sammeta Dinesh Kumar** — [sammetadineshkumar@gmail.com]
- 🌐 [Portfolio](https://dineshsammeta1234.github.io/)  
- 🔗 [LinkedIn](https://www.linkedin.com/in/dineshsammeta)   
