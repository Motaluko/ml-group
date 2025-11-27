from flask import Flask, request, render_template
import joblib
import numpy as np
import os

app = Flask(__name__)

MODEL_PATH = "house_price_model.pkl"

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found: {MODEL_PATH}. Put it in the project folder.")

model = joblib.load(MODEL_PATH)

@app.route("/")
def home():
    return render_template("index.html", result=None, error=None)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Read form inputs and convert to float
        features = [
            float(request.form["MedInc"]),
            float(request.form["HouseAge"]),
            float(request.form["AveRooms"]),
            float(request.form["AveBedrms"]),
            float(request.form["Population"]),
            float(request.form["AveOccup"]),
            float(request.form["Latitude"]),
            float(request.form["Longitude"]),
        ]
    except Exception as e:
        return render_template("index.html", result=None, error="Please enter valid numeric values for all fields.")

    # Predict (model expects shape [1, n_features])
    pred = model.predict([features])[0]

    # The California dataset target is in units of 100,000 (so scale to dollars)
    predicted_price = pred * 100000

    result_text = f"Predicted median house value: ${predicted_price:,.2f}"
    return render_template("index.html", result=result_text, error=None)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=10000)
