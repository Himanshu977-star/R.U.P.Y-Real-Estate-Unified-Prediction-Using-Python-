from flask import Flask, request, render_template
import numpy as np
import pickle

# Load the model and scalers
try:
    model = pickle.load(open('model.pkl', 'rb'))
    sc = pickle.load(open('standscaler.pkl', 'rb'))  # StandardScaler
    mx = pickle.load(open('minmaxscaler.pkl', 'rb'))  # MinMaxScaler
except FileNotFoundError as e:
    raise FileNotFoundError(f"File not found: {e}")
except Exception as e:
    raise RuntimeError(f"An error occurred while loading files: {e}")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
def predict():
    try:
        # Extract form data
        N = float(request.form['Nitrogen'])
        P = float(request.form['Phosporus'])
        K = float(request.form['Potassium'])
        temp = float(request.form['Temperature'])
        humidity = float(request.form['Humidity'])
        ph = float(request.form['pH'])
        rainfall = float(request.form['Rainfall'])

        # Prepare input features
        feature_list = [N, P, K, temp, humidity, ph, rainfall]
        single_pred = np.array(feature_list).reshape(1, -1)

        # Apply MinMaxScaler first, then StandardScaler
        mx_features = mx.transform(single_pred)  # Apply MinMaxScaler
        sc_mx_features = sc.transform(mx_features)  # Apply StandardScaler

        # Make prediction
        prediction = model.predict(sc_mx_features)

        # Map prediction to crop names
        crop_dict = {
            1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut",
            6: "Papaya", 7: "Orange", 8: "Apple", 9: "Muskmelon", 10: "Watermelon",
            11: "Grapes", 12: "Mango", 13: "Banana", 14: "Pomegranate", 15: "Lentil",
            16: "Blackgram", 17: "Mungbean", 18: "Mothbeans", 19: "Pigeonpeas",
            20: "Kidneybeans", 21: "Chickpea", 22: "Coffee"
        }

        crop = crop_dict.get(prediction[0], "Unknown crop")
        result = f"{crop} "

    except Exception as e:
        result = f"An error occurred: {str(e)}"
        
    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)