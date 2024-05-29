from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB connection
client = MongoClient(os.getenv('MONGODB_URI'))
db = client['sample_airbnb']  # Replace with your database name

@app.route('/fetch-data/listingsAndReviews', methods=['GET'])
def fetch_data(collection_name):
    # Access the specified collection
    collection = db[collection_name]

    # Example filter, you can modify this based on your requirements
    filter_criteria = request.args.get('filter', {})

    # Fetch data from MongoDB
    data = list(collection.find(filter_criteria))

    # Perform some operations on data
    filtered_data = [item for item in data if some_condition(item)]  # Replace `some_condition` with your logic

    # Create final response
    response = {
        'status': 'success',
        'data': filtered_data
    }

    return jsonify(response)

def some_condition(item):
    # Define your condition for filtering data here
    return True

if __name__ == '__main__':
    app.run(debug=True)
