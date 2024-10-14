#!/usr/bin/env python3
"""Asynchronous coroutine that takes an integer argument(max_delay), with a different value of 10"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Waits for a random delay seconds"""
    random_number = random.uniform(0, max_delay)
    await asyncio.sleep(random_number)
    return random_number
