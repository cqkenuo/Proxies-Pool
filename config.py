# --*-- coding:utf-8 --*--

import redis

# local databases
MONGO_HOST = "localhost"
MONGO_PORT = 27017
MONGO_DATABASE = "proxy"
MONGO_COLLECTION = "ip_list"
MONGO_USR = "test"
MONGO_PWD = "test"

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_PASSWORD = None

MAX_SCORE = 100
MIN_SCORE = 0
INITIAL_SCORE = 10

# 端口来自 https://proxy.mimvp.com/stat.php#open 统计
PORT_LIST = [8080, 3128, 80, 53281, 4145, 1080, 8118, 8081, 9999,
             8060, 23500, 8888, 9000, 9991, 41258, 808, 83, 443,
             54321, 8181, 63141, 20183, 4153, 64312, 8082, 82,
             9090, 9797, 6666, 8090, 4550, 8000, 8088]


class RedisClient(object):
    # proxies pool
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, pwd=REDIS_PASSWORD):
        """
        initial the Redis
        :param host: Redis host
        :param port: Redis port
        :param pwd: Redis password
        """

        self.db = redis.StrictRedis(host=host, port=port, password=pwd, decode_responses=True)

    def add(self, ):
        pass
