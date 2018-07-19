# This file contains the redis connection class

import redis


class CacheClientConnection(object):
    def __init__(self, logger, host='localhost', port=6379, db=0, *args):
        self._host = host
        self._port = port
        self._db = db
        self._logger = logger

    def get_connection(self):
        try:
            self._logger.info('creating connection to redis')
            conn = redis.StrictRedis(self._host, self._port, self._db)
            self._logger.info('connected to redis')
            return conn
        except Exception as e:
            self._logger.info(e)

        return None
