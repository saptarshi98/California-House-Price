from flask import Flask, request, jsonify
import util
app = Flask(__name__)

@app.route('/predict_price', methods = ['POST'])
def predict_price():
    long = float(request.form['long'])
    lat = float(request.form['lat'])
    age = int(request.form['age'])
    room = int(request.form['room'])
    bedroom = int(request.form['bedroom'])
    population = int(request.form['population'])
    household = int(request.form['household'])
    income = float(request.form['income'])
    proximity = str(request.form['proximity'])

    response = jsonify({
        'estimated_price': util.get_predicted_price(long, lat, age, room, bedroom, population, household, income, proximity)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    print("Starting Flask server for House Price Prediction ...")
    app.run()