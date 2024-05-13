import logging
import json

# Initialize logger
logger = logging.getLogger('DjangoRESTFramework')
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('django_rest_framework_logs.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Example usage
# This would involve setting up Django with DRF and using logging within your Django views or serializers.
# Since it's more complex, I'm not providing an example here.
