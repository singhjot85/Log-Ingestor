import requests
import logging
import json

# Initialize logger
logger = logging.getLogger('Requests')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('requests_logs.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Example usage
logger.info('Making a request to example.com')
response = requests.get('http://example.com')
logger.info(f'Response status code: {response.status_code}')
