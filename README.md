# California House Price Prediction
![Application Screenshot]([app](https://github.com/user-attachments/assets/ed32311a-544a-45b2-ba14-8dba23648930))
This is a Flask web application that predicts house prices in California based on various features using a trained machine learning model.

## Features
- Predict house prices based on:
  - Median Income
  - House Age
  - Average Rooms
  - Average Bedrooms
- Stores prediction history in SQLite database
- Displays prediction history in a table format
- Modern and responsive web interface

## Installation
1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python app.py
   ```
4. Access the application at http://localhost:5000

## Requirements
- Python 3.7+
- Flask
- scikit-learn
- numpy
- sqlite3 (built-in)

## Usage
1. Fill in the form with the required features
2. Click "Predict Price" to get the prediction
3. View prediction history in the table below the form

## Screenshots
1.Input and prediction


## File Structure
```
.
├── app.py              # Main application file
├── house_price_model.pkl  # Trained model
├── model.py            # Model training script
├── README.md           # This file
├── requirements.txt    # Python dependencies
└── templates/          # HTML templates
    └── index.html      # Main template
```


