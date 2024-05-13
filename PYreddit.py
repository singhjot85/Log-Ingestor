import praw
import logging
import json

# Initialize logger
logger = logging.getLogger('PRAW')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('praw_logs.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Example usage
logger.info('Fetching subreddit information')
reddit = praw.Reddit(client_id='client_id', client_secret='client_secret', user_agent='user_agent')
subreddit = reddit.subreddit('python')
for submission in subreddit.hot(limit=5):
    logger.info(f"Title: {submission.title}")
