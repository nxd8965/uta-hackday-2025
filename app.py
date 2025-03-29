from flask import Flask, request, jsonify, render_template
import joblib  # Changed from pickle
import numpy as np

app = Flask(__name__)

# Load the model (make sure model.pkl is in the same directory or adjust the path)
try:
    model = joblib.load('model.pkl')  # Changed from pickle.load
except FileNotFoundError:
    print("Error: model.pkl not found.  Make sure it's in the correct directory.")
    model = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model not loaded. Check server logs.'})

    try:
        # Get the input values from the form
        v1 = float(request.form['V1'])
        v2 = float(request.form['V2'])
        v3 = float(request.form['V3'])
        v4 = float(request.form['V4'])
        v5 = float(request.form['V5'])
        v6 = float(request.form['V6'])
        v7 = float(request.form['V7'])
        v8 = float(request.form['V8'])
        v9 = float(request.form['V9'])
        v10 = float(request.form['V10'])
        v11 = float(request.form['V11'])
        v12 = float(request.form['V12'])
        v13 = float(request.form['V13'])
        v14 = float(request.form['V14'])
        v15 = float(request.form['V15'])
        v16 = float(request.form['V16'])
        v17 = float(request.form['V17'])
        v18 = float(request.form['V18'])
        v19 = float(request.form['V19'])
        v20 = float(request.form['V20'])
        v21 = float(request.form['V21'])
        v22 = float(request.form['V22'])
        v23 = float(request.form['V23'])
        v24 = float(request.form['V24'])
        v25 = float(request.form['V25'])
        v26 = float(request.form['V26'])
        v27 = float(request.form['V27'])
        v28 = float(request.form['V28'])
        amount = float(request.form['Amount'])

        # Create a NumPy array from the input data
        input_data = np.array([[v1, v2, v3, v4, v5, v6, v7, v8, v9, v10,
                                v11, v12, v13, v14, v15, v16, v17, v18, v19, v20,
                                v21, v22, v23, v24, v25, v26, v27, v28, amount]])

        # Make the prediction
        prediction = model.predict(input_data)[0]  # Get the single prediction value

        return jsonify({'prediction': int(prediction)})  # Convert to integer for JSON

    except Exception as e:
        print(f"Error during prediction: {e}")
        return jsonify({'error': str(e)})  # Return the error message

if __name__ == '__main__':
    app.run(debug=True)