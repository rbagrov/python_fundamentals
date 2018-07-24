# This fie contains the persistence client

import threading


class PersistenceClient(object):
    """ This class is responsible for communication between
        the database and the business logic
        :param logger - to log evey actin
        :param connection - which database is used
        :param process - the process that created this object
    """
    def __init__(self, logger, connection):
        self.logger = logger
        self.connection = connection
        self.lock = threading.Lock()

    def create_table(self, sql_command):
        """ This method creates a table in the database specified from connection
            :param sql_command: the sql command for creating a table
        """
        try:
            self.logger.info('{} - creating table'.format(threading.current_thread().name)) # noqa
            self.lock.acquire()
            c = self.connection.cursor()
            c.execute(sql_command)
            self.connection.commit()
            self.lock.release()
            self.logger.info('{} - table created successfully'.format(threading.current_thread().name)) # noqa
        except Exception as e:
            self.logger.info(e)

        return None

    def get_item(self, sql_command, item):
        """ This method get items from the database specified by the connection
            :param sql_command: the sql command to for getting data
            :param item: the item to search for
        """
        try:
            self.logger.info('{} - Getting item'.format(threading.current_thread().name)) # noqa
            c = self.connection.cursor()
            c.execute(sql_command, item)
            result = c.fetchall()
            if not result:
                self.logger.info('{} - Items not found, returning None'.format(threading.current_thread().name)) # noqa
                return None
            else:
                self.logger.info('{} - Found items, returning them'.format(threading.current_thread().name)) # noqa
                return result
        except Exception as e:
            self.logger.info(e)

        return None

    def insert_item(self, sql_command, item):
        """ This method insert items in the database
            specified in the connection
            :param sql_command: sql command for inserting
            :param item: list of values to be inserted
            something in the db
        """
        try:
            self.logger.info('{} - inserting item in table'.format(threading.current_thread().name)) # noqa
            self.lock.acquire()
            c = self.connection.cursor()
            c.execute(sql_command, item)
            self.connection.commit()
            self.lock.release()
            self.logger.info('{} - item successfully added'.format(threading.current_thread().name)) # noqa
        except Exception as e:
            self.logger.info(e)

        return None

    def update_item(self, sql_command, item):
        """ This method updates an item in the db
            specified by the connection
            :param sql_command: sql command for updating item
            :param item: list of values to update
        """
        try:
            self.logger.info('{} - updating item in table'.format(threading.current_thread().name)) # noqa
            self.lock.acquire()
            c = self.connection.cursor()
            c.execute(sql_command, item)
            self.connection.commit()
            self.lock.release()
            self.logger.info('{} - item successfully updated'.format(threading.current_thread().name)) # noqa
        except Exception as e:
            self.logger.info(e)

        return None

    def delete_item(self, sql_command, item):
        """ this method deletes an item from the databes
            specified from the connection
            :param sql_command: sql command to delete item
            :param item: the item to delete
        """
        try:
            self.logger.info('{} - deleting item from table'.format(threading.current_thread().name)) # noqa
            self.lock.acquire()
            c = self.connection.cursor()
            c.execute(sql_command, item)
            self.connection.commit()
            self.lock.release()
            self.logger.info('{} - item successfully deleted'.format(threading.current_thread().name)) # noqa
        except Exception as e:
            self.logger.info(e)

        return None

    def close(self):
        try:
            self.logger.info('{} - closing db connection'.format(threading.current_thread().name)) # noqa
            self.connection.close()
            self.logger.info('{} - connection closed'.format(threading.current_thread().name)) # noqa
        except Exception as e:
            self.logger.info(e)

        return None
