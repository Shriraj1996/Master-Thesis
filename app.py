import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import math

app = Flask(__name__)
model = pickle.load(open('cropyield1.pkl', 'rb'))  #imported model of ML

@app.route('/')   #route folder
def home():
    return render_template('index.html')  # load form html

@app.route('/predict',methods=['POST'])  # function need to run -- same should to be present in HTML 
def predict(): 
	int_features = [int(x) for x in request.form.values()]
	final_features = [np.array(int_features)]
	prediction = model.predict(final_features)
	return render_template('index.html',prediction_text=prediction)
	
if __name__ == "__main__":
    app.run(debug=True)