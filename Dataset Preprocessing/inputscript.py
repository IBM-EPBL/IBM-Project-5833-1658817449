import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
#importing the inputScript file used to analyze the URL
import inputScript
#load model
 app = Flask
              name
model = pickle. loadopen('Phishing_Website.pkl', 'rb') )
#Redirects to the page to give the user iput URL.
@app.route('/predict")
def predict():
     return render_template( 'final.html')
#Fetches the URL given by the URL and passes to inputScript
@app.route('/y_predict',methods=[ 'POST')
def y_predict():
    For rendering results on HTML GUI
     ...
    url = request. form[ 'URL']
    checkprediction = inputScript.main(ur1)
     prediction = model.predict(checkprediction)
     print (prediction)
    output-prediction[0]
    if(output==1):
        pred="Your are safe!! This is a Legitimate Website."
     else:
        pred="You are on the wrong site. Be cautious!"
     return render_template( 'final.html', prediction_text="
#Takes the input parameters fetched from the URL by inputScript and returns the predictions
@ppp.route("/predict_opi ',methods=[ 'POST'])
def predict_api():
    For direct API calls trought request
    data = request.get_json(force=True)
    prediction= model.y_predict([np.array(list(data.values()))D)
    output - prediction[0]
     return
if
      name
             ==
                   main
     app.run (host= '0.0.0.0', debug=True)

