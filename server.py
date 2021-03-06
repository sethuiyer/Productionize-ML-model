from flask import Flask, request, render_template, jsonify
from ml.titanic import Titanic

app = Flask(__name__)


@app.route("/")
def hello():
    return 'Hello, Do you think you would have survived the Titanic Disaster?'


@app.route("/fit")
def train():
    return render_template('fit.html')


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == "GET":
        return render_template('predict.html')
    else:
        data = {
            'PassengerId': 891,
            'Pclass': 3,
            'Name': 'Kelly, Mr.James',
            'Sex':'male',
            'Age':34.5,
            'SibSp':0,
            'Parch':0,
            'Ticket':'330911',
            'Fare':7.82,
            'Cabin':'',
            'Embarked': 'Q',
            }
        data = Titanic.get_probability(data)
        response = {
            'prediction': data
        }
        return jsonify(response)

if __name__ == "__main__":
    app.run("127.0.0.1",debug=True)