# This fie contains the persistence client


class PersistenceClient(object):
    """ This class is responsible for communication between
        the database and the business logic
        :param logger - to log evey actin
        :param connection - which database is used
        :param process - the process that created this object
    """
    def __init__(self, logger, thread, connection):
        self.logger = logger
        self.thread = thread
        self.lock = thread.Lock()
        self.connection = connection

    def create_table(self, sql_command):
        """ This method creates a table in the database specified from connection
            :param sql_command: the sql command for creating a table
        """
        try:
            self.logger.info('creating table')
            self.lock.acquire()
            c = self.connection.cursor()
            c.execute(sql_command)
            self.connection.commit()
            self.connection.close()
            self.lock.release()
            self.logger.info('table created successfully')
        except Exception as e:
            self.logger.info(e)

        return None

    def get_item(self, sql_command, item):
        """ This method get items from the database specified by the connection
            :param sql_command: the sql command to for getting data
            :param item: the item to search for
        """
        try:
            self.logger.info('Getting item')
            c = self.connection.cursor()
            c.execute(sql_command, item)
            result = c.fetchall()
            self.connection.close()
            self.logger.info('Found items, returning them')
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
            self.logger.info('inserting item in table')
            self.lock.acquire()
            c = self.connection.cursor()
            c.execute(sql_command, item)
            self.connection.commit()
            self.connection.close()
            self.lock.release()
            self.logger.info('item successfully added')
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
            self.logger.info('updating item in table')
            self.lock.acquire()
            c = self.connection.cursor()
            c.execute(sql_command, item)
            self.connection.commit()
            self.connection.close()
            self.lock.release()
            self.logger.info('item successfully updated')
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
            self.logger.info('deleting item from table')
            self.lock.acquire()
            c = self.connection.cursor()
            c.execute(sql_command, item)
            self.connection.commit()
            self.connection.close()
            self.lock.release()
            self.logger.info('item successfully deleted')
        except Exception as e:
            self.logger.info(e)

        return None
