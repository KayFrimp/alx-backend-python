#!/usr/bin/env python3
"""measure_runtime Module"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Executes async_comprehension four times in parallel using
    asyncio.gather and measures total runtime."""
    start_time = time.perf_counter()
    awaitables = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*awaitables)
    end_time = time.perf_counter()
    return end_time - start_time
