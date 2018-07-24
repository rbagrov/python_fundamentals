# This file contans the class fetching info from apis

import threading
import logging.config
from queue import Queue
from util.Cache import Cache
from util.CacheClient import CacheClient
from util.CacheClientConnection import CacheClientConnection
from db.Connection import Connection
from db.PersistenceClient import PersistenceClient


logging.config.fileConfig('conf/LoggerConfig.ini')
cache_logger = logging.getLogger('Cache')
cache_conn = CacheClientConnection(cache_logger).get_connection()
cache_client = CacheClient(cache_logger, cache_conn)
cache = Cache(cache_client, cache_logger)

db_file = 'cars.db'


class FetchClient(object):
    def __init__(self, logger, service):
        self.service = service
        self.logger = logger

    def _connection_creator(self):
        """ private method for createing connetions to db """
        try:
            conn_logger = logging.getLogger('Connect')
            db_logger = logging.getLogger('Persistence')
            db_conn = Connection(conn_logger, db_file).connect()
            db = PersistenceClient(db_logger, db_conn)
            return db
        except Exception as e:
            self.logger.info(e)

    def _thread_generator(self, fn, q, *args, **kwargs):
        """ private method for creating threads """
        while not q.empty():
            worker = q.get()
            try:
                if len(args) is not 0:
                    t = threading.Thread(target=fn, args=(args[0][worker],))
                    t.start()
                elif len(kwargs) is not 0:
                    t = threading.Thread(target=fn, args=(kwargs['make_id'][worker], kwargs['model_id'][worker])) # noqa
                    t.start()
            except Exception as e:
                self.logger.info(e)

            q.task_done()
        return None

    def _insert_if_new(self, responce, db, table_name):
        """ private method for checking if item is in db
            and inserting in db if not """
        try:
            for car in responce:
                command = 'SELECT * FROM {} WHERE nome=?'.format(table_name)
                if db.get_item(command, (car['nome'],)) is None:
                    command = 'INSERT INTO {}(nome,codigo) VALUES(?,?)'.format(table_name) # noqa
                    db.insert_item(command, (car['nome'], car['codigo']))
        except Exception as e:
            self.logger.info(e)

        return None

    @cache.cache
    def _fetch_cars_by_make(self, make_id):
        """ private method for fetching data from api with service """
        db = self._connection_creator()
        try:
            self.logger.info('{} - fetching cars woth make id: {}'.format(threading.current_thread().name, make_id)) # noqa
            res = self.service.get_car_models(make_id)
            self._insert_if_new(res['modelos'], db, 'models')
            self.logger.info('{} - data fetched and inserted into db'.format(threading.current_thread().name)) # noqa
            return res['modelos']
        except Exception as e:
            self.logger.info(e)

        return None

    @cache.cache
    def _fetch_cars_by_make_model(self, make_id, model_id):
        """ private method for fetching data from api with service """
        db = self._connection_creator()
        try:
            self.logger.info('{} - fetching cars with make id: {} and model id: {}'.format(threading.current_thread().name, make_id, model_id)) # noqa
            res = self.service.get_car_models_years(make_id, model_id)
            self._insert_if_new(res, db, 'years')
            self.logger.info('{} - data fetched and inseted into db'.format(threading.current_thread().name)) # noqa
            return res
        except Exception as e:
            self.logger.info(e)

        return None

    def fetch_from_cars(self, fetch_type, *args, **kwargs):
        """ method for fetching data from api with service
            @param fetch_type@ tell what endpoint to use
            @params args and kwargs@ args is for fetching with make
            and kwargs is fir fetching with make and model
            the number of params determens the number of fetch requests
        """
        q = Queue()
        if len(args) is not 0:
            for i in range(len(args)):
                q.put(i)

        if len(kwargs) is not 0:
            for i in range(len(kwargs)):
                q.put(i)

        if fetch_type is 'models':
            self._thread_generator(self._fetch_cars_by_make, q, args)
        elif fetch_type is 'years':
            self._thread_generator(self._fetch_cars_by_make_model, q, make_id=kwargs['make_id'], model_id=kwargs['model_id']) # noqa
