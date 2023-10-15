import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app = Flask(__name__)  #it is the starting point of my appliction where it will run.
regmodel = pickle.load(open('regmodel.pkl','rb')) # we are opening the pickle file in read byte mode and loading it.


@app.route('/') # the first route. i.e., in the searchbar if i pass localhost, URL, and slash, it will take me to home page.
def home():
    return render_template('home.html') #entering home, a html page welcome audience would be there.


#creating a predict api using postman to send input to our model and our model gives us the response for that input.
@app.route('/predict_api', methods = ['Post'])

