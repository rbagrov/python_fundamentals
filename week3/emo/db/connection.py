# This file contains db configuration
import redis

HOST = 'localhost'
PORT= 6379
DB = 0

connection = redis.StrictRedis(host=HOST, port=PORT, db=DB)
