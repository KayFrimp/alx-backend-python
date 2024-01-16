#!/usr/bin/env python3
"""measure_time Module"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Computes the average runtime of wait_n.

    Syntax: measure_time(n, max_delay)

    Args:
        n (int): argument for wait_n
        max_delay (int): argument for wait_n

    Return (float): total execution time"""
    initial_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - initial_time
    return total_time / n
