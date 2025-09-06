from signal_processing import process_signal, symbolic_transforms

# Test symbolic transforms
lap, four = symbolic_transforms('sin(t)')
print('Laplace:', lap)
print('Fourier:', four)

# Test signal processing
results = process_signal('synthetic')
print('Generated files:', list(results.keys()))
