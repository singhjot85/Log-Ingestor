import requests

# Define the base URL of the Flask app
BASE_URL = 'http://127.0.0.1:5000'

# Function to send GET request to fetch all data
def get_all_data():
    response = requests.get(BASE_URL + '/data')
    return response.json()

# Function to send GET request to fetch data by ID
def get_data_by_id(data_id):
    response = requests.get(BASE_URL + f'/data/{data_id}')
    return response.json()

# Function to send PUT request to update data by ID
def update_data(data_id, new_data):
    response = requests.put(BASE_URL + f'/data/{data_id}', json=new_data)
    return response.json()

if __name__ == '__main__':
    # Fetch all data
    all_data = get_all_data()
    print("All Data:", all_data)

    # Fetch data by ID
    data_id = '1'
    data_by_id = get_data_by_id(data_id)
    print("Data by ID:", data_by_id)

    # Update data by ID
    updated_data = {'name': 'Charlie', 'age': 35}
    update_response = update_data(data_id, updated_data)
    print("Update Response:", update_response)

    # Fetch updated data by ID
    updated_data_by_id = get_data_by_id(data_id)
    print("Updated Data by ID:", updated_data_by_id)
