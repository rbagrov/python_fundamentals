# This file contains the redis client


class CacheClient(object):
    def __init__(self, logger, connection, *args):
        self.connection = connection
        self.logger = logger

    def get_item(self, key):
        """ method for getting items from cache """
        try:
            self.logger.info('retrieving item from cache')
            res = self.connection.get(key)
            return res
        except Exception as e:
            self.logger.info(e)

        return None

    def put_item(self, key, item):
        """ method for putting items in cache """
        try:
            self.logger.info('puting item in cache')
            self.connection.set(key, item)
            self.logger.info('item put in cache')
            return None
        except Exception as e:
            self.logger.info(e)

        return None

    def invalidate_item(self, key, time):
        """ method for invalidating items in cache """
        try:
            self.logger.info('setting {}\'s TTL for item'.format(time))
            self.connection.expire(key, time)
            self.logger.info('TTL set')
            return None
        except Exception as e:
            self.logger.info(e)

        return None
