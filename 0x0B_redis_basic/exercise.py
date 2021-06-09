#!/usr/bin/env python3
""" 0x0B. Redis basic """
from typing import Callable, Optional, Union
from functools import wraps
import redis
import uuid


def count_calls(method: Callable) -> Callable:
    """increments the count for that key every time the method
    and returns the value returned by the original method. """
    method_ = method.__qualname__

    @wraps(method)
    def wrapper(self, args):
        """ Wrapper method """
        c = method(self, args)
        self._redis.incr(method_)
        return c
    return wrapper


def call_history(method: Callable) -> Callable:
    """ Method stores
    the history of
    inputs and outputs """
    inputs = method.__qualname__ + ":inputs"
    outputs = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args):
        """ Wrapper method """
        self._redis.rpush(inputs, str(args))
        res = method(self, *args)
        self._redis.rpush(outputs, str(res))
        return res
    return wrapper


def replay(method: Callable):
    """ displays the history
    of calls of a particular function
    """
    inst = redis.Redis()
    storage = method.__qualname__
    aux = inst.get(storage).decode('utf-8')
    inputs = inst.lrange(storage + ':inputs', 0, -1)
    outputs = inst.lrange(storage + ':outputs', 0, -1)
    print("{} was called {} times:".format(storage, aux))
    for inp, out in zip(inputs, outputs):
        print('{}(*{}) -> {}'.format(storage, inp.decode("utf-8"),
                                     out.decode("utf-8")))


class Cache:
    """ Cache class redis"""
    def __init__(self):
        """ init construct """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ generates a random key,
            stores input data
            in Redis using the random key
            and returns the key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable]
            = None) -> Union[str, bytes, int, float]:
        """ converts data
        to a desired format
        """
        data = self._redis.get(key)
        if fn:
            data = fn(data)
        return data

    def get_str(self, key: str) -> Union[str, bytes, int, float]:
        """ converts data
        to string format
        """
        return self.get(key, str)

    def get_int(self, key: str) -> Union[str, bytes, int, float]:
        """ converts data
        to int
        """
        return self.get(key, int)
