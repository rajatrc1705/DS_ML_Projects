import flask
from flask import Flask, jsonify, request
import json
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)

def convertData(X):
    
        
    age = [X[0], 10, 10, 10, 10]
    sex = [X[1], 'male', 'female', 'male', 'female']
    bmi = [X[2], 21, 21, 21, 21]
    smoker = [X[3], 'yes', 'no', 'no', 'no']
    region = [X[4], 'northwest', 'southeast', 'southwest', 'northeast']
    children = [X[5], 1, 2, 3, 4]
    data = pd.DataFrame({
            'age': age,
            'bmi': bmi,
            'children': children,
            'sex': sex,
            'smoker': smoker,
            'region': region
        })
    data_d = pd.get_dummies(data, columns=['sex', 'smoker', 'region'])
    l = data_d.iloc[0, :]
    # print(data_d)
    # print(l, list(l))
    reshaped_values = np.array(l)
    return reshaped_values

@app.route('/predict', methods=['GET'])
def predict():
    
    x = [49, 'male', 21, 'no',  'northwest', 2]
    model = load_models()
    
    request_json = request.get_json()
    x = request_json['input']
    x = list(x)
    data_input = convertData(x)
    data_input_reshaped = data_input.reshape(1, -1)
    prediction = model.predict(data_input_reshaped)[0]
    
    response = json.dumps({'charges': prediction})

    return response, 200

def load_models():
    file_name = "models/model_file.p"
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data['model']
    return model

if __name__ == '__main__':
    application.run(debug=True)