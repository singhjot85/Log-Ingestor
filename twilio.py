from twilio.rest import Client
import logging
import json

# Initialize logger
logger = logging.getLogger('Twilio')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('twilio_logs.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Example usage
logger.info('Sending SMS')
client = Client("account_sid", "auth_token")
message = client.messages.create(to="your_phone_number", from_="your_twilio_number", body="Hello, this is a test SMS!")
logger.info(f"SMS SID: {message.sid}")
