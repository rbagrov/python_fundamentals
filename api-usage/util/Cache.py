# This file contains the cache decorator


import functools
import hashlib
import threading

DEFAULT_EXPIRATION = 3600


class Cache(object):
    """ Class implementing cache using redis """
    def __init__(self, client, logger):
        self.client = client
        self.logger = logger
        self.lock = threading.Lock()

    def cache(self, fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            fn_hash = self._generate_cache_key(fn, args, kwargs)
            try:
                cache_responce = self.client.get_item(fn_hash)
                if cache_responce is None:
                    self.logger.info('{} - item not found in cache'.format(threading.current_thread().name)) # noqa
                    self.logger.info('calling {}'.format(fn.__name__))
                    res = fn(*args, **kwargs)
                    self.logger.info('{} - caching response from {}'.format(threading.current_thread().name, fn.__name__)) # noqa
                    self.lock.acquire()
                    self.client.put_item(fn_hash, res)
                    self.lock.release()
                    self.client.invalidate_item(fn_hash, DEFAULT_EXPIRATION)
                    return res
                else:
                    self.logger.info('{} - item in cache'.format(threading.current_thread().name))  # noqa
                    return cache_responce
            except Exception as e:
                self.logger.info(e)
        return wrapper

    def _generate_cache_key(self, fn, fn_args=None, fn_kwargs=None):
        """ private method - generates key for item """
        fn_args = fn_args or []
        fn_kwargs = fn_kwargs or {}
        fn_name = fn.__name__
        fn_signature = self._signature_generator(fn_args, **fn_kwargs)
        fn_hash = str(hashlib.sha1((fn_name + fn_signature).encode()).hexdigest()) # noqa
        return fn_hash

    def _signature_generator(self, *args, **kwargs):
        """ private method - returns string with joined fn params """
        parsed_args = ",".join(map(str, args))

        parsed_kwargs = ",".join(
            map(lambda x: '%s=%s' % (x, str(kwargs[x])), kwargs)
        )

        parsed = filter(
            lambda x: x != '', [parsed_args, parsed_kwargs]
        )

        return ','.join(parsed)
