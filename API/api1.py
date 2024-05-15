import requests
import logging

# Initialize logger
logger = logging.getLogger('Flask_APP_Log')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('Flask.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Configure logging
#logging.basicConfig(filename='log1.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

BASE_URL = 'http://127.0.0.1:5000'

def get_all_data():
    response = requests.get(BASE_URL + '/data')
    data = response.json()
    logger.info("GET request to fetch all data successful")
    return data

def get_data_by_id(data_id):
    response = requests.get(BASE_URL + f'/data/{data_id}')
    data = response.json()
    logger.info(f"GET request to fetch data by ID '{data_id}' successful")
    return data

# Function to send PUT request to update data by ID
def update_data(data_id, new_data):
    response = requests.put(BASE_URL + f'/data/{data_id}', json=new_data)
    updated_data = response.json()
    logger.info(f"PUT request to update data by ID '{data_id}' successful")
    return updated_data

if __name__ == '__main__':
    try:
        all_data = get_all_data()
        print("All Data:", all_data)

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

    except Exception as e:
        # If an exception occurs, log the error message
        logging.error(f"Error occurred: {str(e)}")
