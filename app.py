import os
from flask import Flask, render_template, request
from src.signal_analysis import process_signal, symbolic_transforms

app = Flask(__name__)
RESULTS_DIR = os.path.join("static", "results")

@app.route("/", methods=["GET", "POST"])
def index():
    results = {}
    if request.method == "POST":
        expr = request.form.get("expression")  # symbolic expression (e.g., sin(t), exp(-t))
        signal_type = request.form.get("signal_type")  # noisy_ecg / synthetic
        
        # Symbolic Laplace & Fourier
        if expr:
            results["laplace"], results["fourier"] = symbolic_transforms(expr)

        # Numerical Signal Analysis (FFT, filtering, plots)
        if signal_type:
            plots = process_signal(signal_type, RESULTS_DIR)
            results.update(plots)

    return render_template("index.html", results=results)


if __name__ == "__main__":
    if not os.path.exists(RESULTS_DIR):
        os.makedirs(RESULTS_DIR)
    app.run(debug=True)
