#!/usr/bin/env python3
""" 0x0B. Redis basic """
from typing import Callable, Optional, Union
import redis
import uuid


class Cache:
    """ class contains
    and cache """
    def __init__(self):
        """ Method Construct """
        self.__redis = redis.Redis()
        self.__redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Generate and
        random key method """
        id = str(uuid.uuid4())
        self.__redis.set(id, data)
        return id
