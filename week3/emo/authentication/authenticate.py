# This file contains authentication helpers
from db.client import Client
from loggerConfig import logging
from db.connection import connection

logger = logging.getLogger(__name__)
client = Client(connection)

def authenticate(passwordLength=8):
    """ This method authenticates the user before he is put into the database """
    def outer_wrapper(func):
        def wrapper(user, *args, **kwargs):
            logger.info('checking to so if {} is valid'.format(user['username']))
            if len(user['password']) > passwordLength:
                logger.info('Authenticating user')
                userExists = client.getItem(user['username'])
                if userExists is None:
                    logger.info('access granted')
                    func(user, client, *args, **kwargs)
                else:
                    logger.info('{} is already in the database'.format(user['username']))
            else:
                logger.info('password must be longer than {}'.format(passwordLength))

        return wrapper
    return outer_wrapper
