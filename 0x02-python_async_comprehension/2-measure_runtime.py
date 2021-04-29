#!/usr/bin/env python3
""" four parallel comprehensions """
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """  measure the total runtime and return it """
    begin = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    finish = time.time()
    return finish - begin
