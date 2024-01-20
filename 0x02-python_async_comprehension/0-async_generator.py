#!/usr/bin/env python3
"""async_generator Module"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Loops 10 times and yields random number asynchronously"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
