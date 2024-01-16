#!/usr/bin/env python3
"""wait_random Module"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Function waits for a random delay between 0 & max_delay
    Syntax: wait_random(max_delay)
    Args:
        max_delay (int): defaults to 10

    Return (float): random delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
