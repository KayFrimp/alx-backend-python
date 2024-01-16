#!/usr/bin/env python3
"""wait_n Module"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Executes wait_random function n times

    Syntax: wait_n(n, max_delay)

    Args:
        n (int): number of times to run wait_random
        max_delay (int): argument for wait_random function

    Return (List[float]): All randomly generated delays"""
    delay_list = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(delay_list)
