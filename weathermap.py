import pyowm
import logging
import json

# Initialize logger
logger = logging.getLogger('OpenWeatherMap')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('openweathermap_logs.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Example usage
logger.info('Fetching weather information')
owm = pyowm.OWM('your_api_key')
observation = owm.weather_at_place('London,uk')
weather = observation.get_weather()
logger.info(f"Temperature in London: {weather.get_temperature('celsius')['temp']}°C")
