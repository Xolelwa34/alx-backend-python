#!/usr/bin/env python3
""" Executes multiple coroutines at the same time with async """
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Async routine list of all the delays random float.
    """
    run: List[float] = []
    orderList: List[float] = []

    for i in range(n):
        run.append(wait_random(max_delay))

    for o in asyncio.as_completed(delays):
        orderList.append(await o)

    return orderList
