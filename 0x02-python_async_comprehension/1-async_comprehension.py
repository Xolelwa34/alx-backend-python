#!/usr/bin/env python3
""" Async generator from the previous task """
import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
        async generates numbers with comprehension

        Args:
            void

        Return:
            float random numbers
    """
    async def async_comprehension():
    result = [item async for item in async_generator()]
    return result[:10]

async def main():
    result = await async_comprehension()
    print(result)

asyncio.run(main())
