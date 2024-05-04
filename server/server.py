from flask import Flask, request, jsonify
import util
from util import get_estimated_price
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)


@app.route('/get_location_names', methods = ['GET'])
def get_location_names():
    response = jsonify({
        'locations':util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        data = request.json
        total_sqft = float(data.get('total_sqft'))
        location = data.get('location')
        bhk = int(data.get('bhk'))
        bath = int(data.get('bath'))

        if not all([total_sqft, location, bhk, bath]):
            raise ValueError("Missing required parameters")

        estimated_price = util.get_estimated_price(location, total_sqft, bhk, bath)
        response = jsonify({'estimated_price': estimated_price})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        error_message = str(e) if str(e) else "An error occurred while processing the request"
        return jsonify({'error': error_message}), 400
 
 
port = os.getenv("PORT")   
    
if __name__ == "__main__":
    print("Starting server for AI prediction")
    util.load_saved_artifacts()
    print(util.get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
    app.run(port=int(port))
    

    

    