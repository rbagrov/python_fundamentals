# This file contains the cache decorator


import functools
import hashlib
from datetime import datetime


DEFAULT_EXPIRATION = 60


class Cache(object):
    def __init__(self, client, logger):
        self.client = client
        self.logger = logger

    def cache(self, fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            fn_hash = self._generate_cache_key(fn, args, kwargs)
            try:
                cache_responce = self.client.get_item(fn_hash)
                if cache_responce is None:
                    self.logger.info('item not found in cache')
                    self.logger.info('calling {}'.format(fn.__name__))
                    res = fn(*args, **kwargs)
                    time_cached = datetime.now().strftime('%Y-%m-%d %H:%M:%S"')
                    res['time_cached'] = time_cached
                    self.logger.info('caching response from {}'.format(fn.__name__)) # noqa
                    self.client.put_item(fn_hash, res)
                    self.client.invalidate_item(fn_hash, DEFAULT_EXPIRATION)
                    return res
                else:
                    self.logger.info('item in cache')
                    return cache_responce
            except Exception as e:
                self.logger.info(e)
        return wrapper

    def _generate_cache_key(self, fn, fn_args=None, fn_kwargs=None):
        fn_args = fn_args or []
        fn_kwargs = fn_kwargs or {}
        fn_name = fn.__name__
        fn_signature = self._signature_generator(fn_args, **fn_kwargs)
        fn_hash = str(hashlib.sha1((fn_name + fn_signature).encode()).hexdigest()) # noqa
        return fn_hash

    def _signature_generator(self, *args, **kwargs):
        parsed_args = ",".join(map(str, args))

        parsed_kwargs = ",".join(
            map(lambda x: '%s=%s' % (x, str(kwargs[x])), kwargs)
        )

        parsed = filter(
            lambda x: x != '', [parsed_args, parsed_kwargs]
        )

        return ','.join(parsed)
