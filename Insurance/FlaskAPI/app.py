import flask
from flask import Flask, jsonify, request, render_template
import json
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__, template_folder='templates')

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
    print(l, list(l))
    reshaped_values = np.array(l)
    return reshaped_values

@app.route('/', methods=['GET','POST'])
def home():
    
    if request.method == 'POST':
        
        model = load_models()
    
        age_f = request.form.get('age')
        bmi_f = request.form.get('bmi')
        children_f = request.form.get('children')
        sex_f = request.form.get('sex')
        smoker_f = request.form.get('smoker')
        region_f = request.form.get('region')
        
        parameter_list = list([age_f, sex_f, bmi_f, smoker_f,  region_f, children_f])
        print("\nParameter List: {}\n".format(parameter_list))
        data_input = convertData(parameter_list)
        data_input_reshaped = data_input.reshape(1, -1)
        print(data_input)
        print(data_input_reshaped)
        print(data_input_reshaped.shape)
        prediction = model.predict(data_input_reshaped)[0]
        
        print(prediction)
        
        return render_template('index.html', pred=prediction)
    return render_template('index.html', pred='')

@app.route('/predict', methods=['POST'])
def predict():
    
    print(2)
    
    # getting the data from POST request
    request_json = request.get_json()
    x = request_json['input']
    
    print("REQUEST JSON: {}".format(x))
    
    # custom input for testing
    # x = [49, 'male', 21, 'no',  'northwest', 2]
    # Loading the model
    model = load_models()
    
    # converting the data to required format
    x = list(x)
    data_input = convertData(x)
    data_input_reshaped = data_input.reshape(1, -1)
    prediction = model.predict(data_input_reshaped)[0]
    
    # response = json.dumps({'charges': prediction})
    print("Charges: ${:.2f}".format(prediction))
    
    return jsonify(prediction)
    # return response
    # return render_template('index.html', pred=prediction)
    # return response, 200

def load_models():
    file_name = "models/model_file.p"
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data['model']
    return model

if __name__ == '__main__':
    print("Yaha aya")
    application.run(port=3000, debug=True)