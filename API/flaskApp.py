from flask import Flask, jsonify, request
import csv

app = Flask(__name__)

data = {}

def load_data_from_csv():
    with open('Database\Students1.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Extracting relevant data fields
            name = row['NAME OF THE STUDENT']
            university = row['UNIVERSITY']
            total_score = float(row['TOTAL SCORE (OUT of 100)'])  # Assuming score is stored as float
            
            # Creating a unique ID using name and university (for demonstration purposes)
            student_id = f"{name}_{university}"
            
            # Storing relevant data fields in the data dictionary
            data[student_id] = {'name': name, 'university': university, 'total_score': total_score}


load_data_from_csv()

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data)

@app.route('/data/<string:id>', methods=['GET'])
def get_data_by_id(id):
    if id in data:
        return jsonify(data[id])
    else:
        return jsonify({'error': 'Data not found'}), 404

# UPDATE request to update data by ID
@app.route('/data/<string:id>', methods=['PUT'])
def update_data(id):
    if id in data:
        req_data = request.get_json()
        data[id]['name'] = req_data.get('name', data[id]['name'])
        data[id]['age'] = req_data.get('age', data[id]['age'])
        return jsonify({'message': 'Data updated successfully'})
    else:
        return jsonify({'error': 'Data not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)