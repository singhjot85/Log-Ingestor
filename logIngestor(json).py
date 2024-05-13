import logging
import json
from datetime import datetime

class LogIngestor:
    def __init__(self, config_file):
        with open(config_file, 'r') as f:
            self.config = json.load(f)
        self.loggers = {}

    def initialize_loggers(self):
        for api, settings in self.config.items():
            logger = logging.getLogger(api)
            logger.setLevel(settings['level'])
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            file_handler = logging.FileHandler(settings['file_path'])
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
            self.loggers[api] = logger

    def log(self, api, level, log_string):
        try:
            if api in self.loggers:
                # Create log dictionary
                log_data = {
                    "level": logging.getLevelName(level),
                    "log_string": log_string,
                    "timestamp": datetime.utcnow().isoformat() + 'Z',
                    "metadata": {
                        "source": self.config[api]['file_path']
                    }
                }
                # Log the dictionary as a JSON string
                self.loggers[api].error(json.dumps(log_data))
            else:
                raise ValueError(f"API '{api}' is not configured for logging.")
        except Exception as e:
            # Log the error to a separate error log file
            error_logger = logging.getLogger('error_logger')
            error_logger.error(f"Error occurred while logging for API '{api}': {e}")

# Example usage:
config_file = 'api_logging_config.json'  # Path to your JSON configuration file
ingestor = LogIngestor(config_file)
ingestor.initialize_loggers()

# Example usage: Log some messages from different APIs
ingestor.log('API1', logging.INFO, 'Sample log message from API1')
ingestor.log('API2', logging.INFO, 'Sample log message from API2')
ingestor.log('API3', logging.INFO, 'Sample log message from API3')
ingestor.log('API4', logging.INFO, 'Sample log message from API4')
ingestor.log('API5', logging.INFO, 'Sample log message from API5')
ingestor.log('API6', logging.INFO, 'Sample log message from API6')
ingestor.log('API7', logging.INFO, 'Sample log message from API7')
ingestor.log('API8', logging.INFO, 'Sample log message from API8')
ingestor.log('API9', logging.INFO, 'Sample log message from API9')

# Placeholder if nothing is logged
if not any(logger.hasHandlers() for logger in ingestor.loggers.values()):
    default_log = {
        "level": "error",
        "log_string": "No logs recorded.",
        "timestamp": datetime.utcnow().isoformat() + 'Z',
        "metadata": {
            "source": "placeholder.log"
        }
    }
    # Writing default log to a JSON file
    with open('default_log.json', 'w') as f:
        json.dump(default_log, f)
