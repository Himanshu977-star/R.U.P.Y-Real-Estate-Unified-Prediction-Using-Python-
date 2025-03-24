from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import json

# Load trained model
model = pickle.load(open("bangalore_home_prices_model.pickle", "rb"))

# Load column names from JSON file
try:
    with open("columns.json", "r") as f:
        data = json.load(f)
        if "data_columns" in data:
            data_columns = data["data_columns"]
        else:
            raise ValueError("Missing 'data_columns' key in JSON file")
except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
    print(f"Error loading columns.json: {e}")
    data_columns = ["total_sqft", "bath", "bhk"]  # Default columns

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', columns=data_columns)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect user input based on column order
        features = [0] * len(data_columns)  # Initialize feature vector with zeros
        
        for i, col in enumerate(data_columns):
            if col in request.form:
                features[i] = float(request.form[col])
        
        features_array = np.array([features])
        
        # Make prediction
        prediction = model.predict(features_array)
        predicted_price = round(prediction[0], 2)
        
        return render_template('index.html', prediction_text=f'Estimated House Price: ₹{predicted_price} L', columns=data_columns)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
