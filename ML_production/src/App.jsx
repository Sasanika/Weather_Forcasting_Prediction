import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchPrediction = async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await axios.post('http://localhost:5000/predict', {
        temperature_C: 20.1,
        apparent_temperature_C: 19.5,
        humidity: 0.6,
        wind_speed_kmPerH: 10.2,
        wind_bearing_degrees: 180,
        visibility_km: 10.0,
        loud_cover: 0,
        pressure_millibars: 1013.25,
        precip_type: 1,
        year: 2022,
        month: 12,
        day: 31,
        hour: 23
      });
      setPrediction(response.data.prediction);
    } catch (error) {
      setError(error.message);
    }
    setLoading(false);
  };

  return (
    <div>
      <h1>Weather Prediction</h1>
      <button onClick={fetchPrediction} disabled={loading}>
        {loading ? 'Loading...' : 'Predict'}
      </button>
      {error && <div>Error: {error}</div>}
      {prediction && <div>Prediction: {prediction}</div>}
    </div>
  );
}

export default App;
