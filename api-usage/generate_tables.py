import logging.config
from db.Connection import Connection
from db.PersistenceClient import PersistenceClient


logging.config.fileConfig('conf/LoggerConfig.ini')
conn_logger = logging.getLogger('Connection')
persistence_logger = logging.getLogger('PersistenceClient')
conn = Connection(conn_logger, 'cars.db').connect()
persistenceClient = PersistenceClient(persistence_logger, conn)


def create_tables(name):
    return 'Create TABLE {}(id integer PRIMARY KEY, nome text, codigo text)'.format(name) # noqa


tables = ['years', 'models']

try:
    for name in tables:
        persistenceClient.create_table(create_tables(name))
    print('tables created')
except Exception as e:
    print(e)
