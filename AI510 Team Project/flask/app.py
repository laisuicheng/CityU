from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import os
import pandas as pd

app = Flask(__name__)

#load model once used by all prediction calls
model = joblib.load('restaurant_recommendation_model.joblib')


@app.route('/')
def home():
    return render_template('index.html')



@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        features = np.array(data['features']).reshape(1, -1)
        prediction = model.predict(features)
        return jsonify({'prediction': int(prediction[0])})
    except Exception as e:
        return jsonify({'error': str(e)}), 400
"""

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the data from the POST request
        data = request.get_json(force=True)
        # Convert data into DataFrame
        df = pd.DataFrame(data)
        # Make predictions
        predictions = model.predict(df)
        # Convert predictions to list
        predictions_list = predictions.tolist()
        # Return predictions as JSON
        return jsonify(predictions_list)
    except Exception as e:
        return jsonify({'error': str(e)}), 400
"""
 
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
