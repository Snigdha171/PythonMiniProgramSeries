# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 14:05:35 2021

@author: Prachi Prakash
"""

from flask import Flask, request, render_template
import pickle
import numpy as np

# Loading the pickle file
app = Flask(__name__)
model = pickle.load(open('lrm_advertising.pkl', 'rb'))

# Default page
@app.route('/')
def home():
    return render_template('index.html')
    
# Routing to predicting sales    
@app.route('/predict',methods=['POST'])
def predict():

    inputs = [int(x) for x in request.form.values()]
    inputs_final = [np.array(inputs)]
    prediction = model.predict(inputs_final)
    output = prediction[0]

    return render_template('index.html', sales_prediction_value='Forecasted sales : $ {}'.format(round(output[0],2)))

# Starting the script
if __name__ == "__main__":
    app.run(debug=True)