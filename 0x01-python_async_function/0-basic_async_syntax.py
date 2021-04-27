#!/usr/bin/env python3
""" async """
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ max_delay (included and float value)
    seconds and eventually returns it.
    """
    j = random.uniform(0, max_delay)
    await asyncio.sleep(j)
    return j
