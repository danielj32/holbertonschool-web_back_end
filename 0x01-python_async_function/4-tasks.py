#!/usr/bin/env python3
""" 4 tasks """
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) ->List[float]:
    """ task_wait_random is being called """
    tempo: List[float] = []
    for _ in range(n):
        tempo.append(task_wait_random(max_delay))
    return [await tempo for tempo in asyncio.as_completed(tempo)]
