import pymongo
import logging
import json

# Initialize logger
logger = logging.getLogger('PyMongo')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('pymongo_logs.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Example usage
logger.info('Fetching document from MongoDB')
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["mycollection"]
document = collection.find_one()
logger.info(f"Document: {document}")
