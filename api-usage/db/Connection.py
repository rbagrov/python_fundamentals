# This file contains db connection creator

import sqlite3

# The connecion is in RAM memory for now


class Connection(object):
    def __init__(self, logger, db_file):
        """ This method is used for creating a database connection
            :param db_file: containing the name of the db file
            :return: connection or None
        """
        self.db_file = db_file
        self.logger = logger

    def connect(self):
        try:
            self.logger.info('connecting to database')
            conn = sqlite3.connect(self.db_file)
            self.logger.info('connection successfully created')
            return conn
        except Exception as e:
            self.logger.info(e)

    def commit(self):
        try:
            self.logger.info('commiting action to database')
            self.conn.commit()
            self.logger.info('commited successfully')
        except Exception as e:
            self.logger.info(e)

        return None

    def close(self):
        try:
            self.logger.info('closing connection to database')
            self.conn.close()
            self.logger.info('connection to database closed')
        except Exception as e:
            self.logger.info(e)

        return None
