import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# Create flask app
model = pickle.load(open("model.pkl", "rb"))
flask_app = Flask(__name__,template_folder="templates",static_folder='static')

@flask_app.route("/")
def home():
    return render_template("index.html")
@flask_app.route("/predict", methods = ["POST"])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)
    return render_template("index.html", prediction_text = "The Zomato Restaurant Rating is {}".format(prediction))

# if __name__ == "__main__":
#     flask_app.run(host="0.0.0.0",port=8080)

if __name__=='__main__':
    flask_app.run(debug=True)