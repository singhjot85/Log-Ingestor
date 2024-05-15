from github import Github
import logging
import json

# Initialize logger
logger = logging.getLogger('PyGithub')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('pygithub_logs.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Example usage
logger.info('Fetching repository information')
g = Github("")
repo = g.get_repo("https://github.com/singhjot85/Log-Ingestor.git")
logger.info(f'Repository full name: {repo.full_name}')
