import logging.config
from services.CarsService import CarsService
from Client import Client


logging.config.fileConfig('conf/LoggerConfig.ini')
client_logger = logging.getLogger('Client')
service = CarsService()
client = Client(client_logger, service)

# Example usage of fetch models
""" the number of make_id's determens how many operations are made
fetch_type = 'models'
print(client.fetch_from_cars(fetch_type, 1, 233, 52, 511))
"""

# Example usage of fetvh years
""" the number of params in make_id nad model_id determens how many operations are made
fetch_type = 'years'
client.fetch_from_cars(fetch_type, make_id=('59', '59'), model_id=('5940', '5940'))
"""
