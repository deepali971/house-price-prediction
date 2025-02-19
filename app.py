from flask import Flask, render_template, request
import joblib
import numpy as np
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Initialize database
def init_db():
    conn = sqlite3.connect('predictions.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS predictions
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  timestamp TEXT,
                  medinc REAL,
                  houseage REAL,
                  averooms REAL,
                  avebedrms REAL,
                  prediction REAL)''')
    conn.commit()
    conn.close()

# Load the trained model
model = joblib.load('house_price_model.pkl')

def save_prediction(data, prediction):
    """Save prediction data to SQLite database"""
    conn = sqlite3.connect('predictions.db')
    c = conn.cursor()
    
    c.execute('''INSERT INTO predictions 
                 (timestamp, medinc, houseage, averooms, avebedrms, prediction)
                 VALUES (?, ?, ?, ?, ?, ?)''',
              (datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
               data['MedInc'],
               data['HouseAge'],
               data['AveRooms'],
               data['AveBedrms'],
               prediction))
    conn.commit()
    conn.close()

def get_predictions():
    """Retrieve all predictions from database"""
    conn = sqlite3.connect('predictions.db')
    c = conn.cursor()
    c.execute('SELECT * FROM predictions ORDER BY timestamp DESC')
    predictions = c.fetchall()
    conn.close()
    return predictions

@app.route('/')
def home():
    predictions = get_predictions()
    return render_template('index.html', predictions=predictions)

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data and map to correct feature order
    form_data = {
        'MedInc': float(request.form['medinc']),
        'HouseAge': float(request.form['houseage']),
        'AveRooms': float(request.form['averooms']),
        'AveBedrms': float(request.form['avebedrms'])
    }

    # Convert to array in correct feature order
    features = [form_data['MedInc'], form_data['HouseAge'], 
                form_data['AveRooms'], form_data['AveBedrms']]
    final_features = [np.array(features)]

    # Make prediction
    prediction = model.predict(final_features)
    
    # Format the output
    output = round(prediction[0], 2)
    
    # Save prediction to database
    save_prediction(form_data, output)
    
    # Get updated predictions
    predictions = get_predictions()
    
    return render_template('index.html', 
                         prediction_text=f'Predicted House Price: ${output:,}',
                         predictions=predictions)

# Initialize database when starting the app
init_db()

if __name__ == '__main__':
    app.run(debug=True)
