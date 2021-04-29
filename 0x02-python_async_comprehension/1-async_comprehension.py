#!/usr/bin/env python3
""" 1. Async Comprehensions """
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ return the 10 random numbers. """
    return [j async for j in async_generator()]
