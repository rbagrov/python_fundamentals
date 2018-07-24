# Testing FetchClient
# import logging.config
# from services.CarsService import CarsService
# from FetchClient import FetchClient


# logging.config.fileConfig('conf/LoggerConfig.ini')
# client_logger = logging.getLogger('Client')
# service = CarsService()
# fetch_client = FetchClient(client_logger, service)

# Example usage of fetch models
""" the number of make_id's determens how many operations are made
fetch_type = 'models'
fetch_client.fetch_from_cars(fetch_type, '1', '233', '52', '511', '1')
"""

# Example usage of fetvh years
""" the number of params in make_id nad model_id
    determens how many operations are made

fetch_type = 'years'
fetch_client.fetch_from_cars(fetch_type, make_id=('59', '59'),
                       model_id=('5940', '5940'))
"""

# Testing GetClient
# from db.Connection import Connection
# from db.PersistenceClient import PersistenceClient
# from GetClient import GetClient


# conn_logger = logging.getLogger('Connection')
# db_logger = logging.getLogger('Persistence')
# client_logger = logging.getLogger('Client')
# db_file = 'cars.db'
# conn = Connection(conn_logger, db_file).connect()
# db = PersistenceClient(db_logger, conn)
# get_client = GetClient(client_logger, db)
""" make your queries and run get
    with the query and params needed for query """
# command = 'SELECT * FROM years'
# print(get_client.get(command, ()))
# print(get_client.get(command, ()))
# print(get_client.get(command, ()))
