#!/usr/bin/env python3
""" async multiple coroutines"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ execute multiple coroutines at the same time with async
    """
    m_lista: List[float]
    m_lista = []

    for _ in range(n):
        m_lista.append(wait_random(max_delay))
    return [await m_lista for m_lista in asyncio.as_completed(m_lista)]
