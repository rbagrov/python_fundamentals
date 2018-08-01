# This file contains client for getting info from db

import logging.config
from util.Cache import Cache
from util.CacheClient import CacheClient
from util.CacheClientConnection import CacheClientConnection


logging.config.fileConfig('conf/LoggerConfig.ini')
cache_logger = logging.getLogger('Cache')
cache_conn = CacheClientConnection(cache_logger).get_connection()
cache_client = CacheClient(cache_logger, cache_conn)
cache = Cache(cache_client, cache_logger)


class GetClient(object):
    def __init__(self, logger, db):
        self.db = db
        self.logger = logger

    @cache.cache
    def get(self, command, params):
        """ method for getting data from db """
        try:
            self.logger.info('getting items from db')
            res = self.db.get_item(command, params)
            self.logger.info('items found returning them')
            return res
        except Exception as e:
            self.logger.info(e)
