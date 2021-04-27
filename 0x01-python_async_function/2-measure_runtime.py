#!/usr/bin/env python3
"""  Measure the runtime """
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ function should return a float """
    tempo = time.time()
    asyncio.run(wait_n(n, max_delay))
    total = time.time() - tempo
    return total / n
