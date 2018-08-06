# This file contains db connection creator

import sqlite3
import threading


class Connection(object):
    def __init__(self, logger, db_file):
        """ This method is used for creating a database connection
            :param db_file: containing the name of the db file
            :return: connection or None
        """
        self.db_file = db_file
        self.logger = logger

    def connect(self):
        """ This method creates and return a db connection """
        try:
            self.logger.info('{} - connecting to database'.format(threading.current_thread().name)) # noqa
            conn = sqlite3.connect(self.db_file)
            self.logger.info('{} - connection successfully created'.format(threading.current_thread().name)) # noqa
            self.conn = conn
            return conn
        except Exception as e:
            self.logger.info(e)

        return None

    def commit(self):
        """ This method commits actions to db """
        try:
            self.logger.info('{} - commiting action to database'.format(threading.current_thread().name)) # noqa
            self.conn.commit()
            self.logger.info('{} - commited successfully'.format(threading.current_thread().name)) # noqa
        except Exception as e:
            self.logger.info(e)

        return None

    def close(self):
        """ This method closes the connection to the db """
        try:
            self.logger.info('{} - closing connection to database'.format(threading.current_thread().name)) # noqa
            self.conn.close()
            self.logger.info('{} - connection to database closed'.format(threading.current_thread().name)) # noqa
        except Exception as e:
            self.logger.info(e)

        return None
