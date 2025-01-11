from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model_path = "artifacts/model_trainer/model.joblib"
with open(model_path, "rb") as file:
    model = joblib.load(file)

# Route for the homepage
@app.route("/")
def index():
    return render_template("index.html")

# Route for making predictions
@app.route("/predict", methods=["POST"])
def predict():
    data = request.form
    # Extract input values from the form
    input_features = [
        float(data['fixed_acidity']),
        float(data['volatile_acidity']),
        float(data['citric_acid']),
        float(data['residual_sugar']),
        float(data['chlorides']),
        float(data['free_sulfur_dioxide']),
        float(data['total_sulfur_dioxide']),
        float(data['density']),
        float(data['pH']),
        float(data['sulphates']),
        float(data['alcohol']),
    ]
    
    # Convert to NumPy array and reshape for prediction
    input_array = np.array(input_features).reshape(1, -1)
    prediction = model.predict(input_array)

    # Return prediction result
    result = "High Quality" if prediction == 1 else "Low Quality"
    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)
