from googleapiclient.discovery import build
import logging
import json

# Initialize logger
logger = logging.getLogger('GoogleAPIs')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('googleapis_logs.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Example usage
logger.info('Fetching YouTube video information')
youtube = build("youtube", "v3", developerKey="your_api_key")
request = youtube.videos().list(part="snippet", chart="mostPopular", maxResults=5)
response = request.execute()
for video in response['items']:
    logger.info(f"Video title: {video['snippet']['title']}")
