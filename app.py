from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS from flask_cors
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes in your Flask app

# Replace the MongoDB URI and Database with your values
mongo_uri = "mongodb+srv://gowtham:Gowtham12345%40@netflix-clone.9thyurk.mongodb.net/netflix"
database_name = "visualskill_newsletter"

client = MongoClient(mongo_uri)
db = client[database_name]

@app.route('/subscribe', methods=['POST'])
def subscribe():
    try:
        data = request.get_json()
        email = data.get('email')

        if email:
            db.subscribers.insert_one({'email': email})
            return jsonify({'message': 'Subscription successful'}), 200
        else:
            return jsonify({'error': 'Email is required'}), 400
    except Exception as e:
        print(f"Error during subscription: {str(e)}")
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
