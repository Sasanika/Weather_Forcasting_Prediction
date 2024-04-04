from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import joblib

app = Flask(__name__)
CORS(app, resources={r"/predict": {"origins": "http://localhost:5173"}})

# Load the machine learning model and the dataset
model = joblib.load('savemodel.sav')
data = pd.read_csv('weatherHistory.csv')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the JSON data from the request
    data = request.get_json()

    # Convert input data to appropriate types
    temperature_C = float(data['temperature_C'])
    apparent_temperature_C = float(data['apparent_temperature_C'])
    humidity = float(data['humidity'])
    wind_speed_kmPerH = float(data['wind_speed_kmPerH'])
    wind_bearing_degrees = int(data['wind_bearing_degrees'])
    visibility_km = float(data['visibility_km'])
    loud_cover = int(data['loud_cover'])
    pressure_millibars = float(data['pressure_millibars'])
    precip_type = int(data['precip_type'])
    year = int(data['year'])
    month = int(data['month'])
    day = int(data['day'])
    hour = int(data['hour'])

    # Create a DataFrame from the input data
    input_data = pd.DataFrame({
        'temperature_C': [temperature_C],
        'apparent_temperature_C': [apparent_temperature_C],
        'humidity': [humidity],
        'wind_speed_kmPerH': [wind_speed_kmPerH],
        'wind_bearing_degrees': [wind_bearing_degrees],
        'visibility_km': [visibility_km],
        'loud_cover': [loud_cover],
        'pressure_millibars': [pressure_millibars],
        'precip_type': [precip_type],
        'year': [year],
        'month': [month],
        'day': [day],
        'hour': [hour]
    })

    # Make predictions using the loaded model
    prediction = model.predict(input_data)

    # Return the prediction as JSON
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
