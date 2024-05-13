import tweepy
import logging
import json

# Initialize logger
logger = logging.getLogger('Tweepy')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('tweepy_logs.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Example usage
logger.info('Fetching user timeline')
auth = tweepy.OAuthHandler('consumer_key', 'consumer_secret')
auth.set_access_token('access_token', 'access_token_secret')
api = tweepy.API(auth)
tweets = api.user_timeline(screen_name='twitter_handle', count=5)
for tweet in tweets:
    logger.info(f'Tweet: {tweet.text}')
