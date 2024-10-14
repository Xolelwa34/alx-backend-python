#!/usr/bin/env python3
""" Takes int arg, waits for random delay """

from typing import List
import asyncio
import random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """ Returns the list of all the delays"""
    spawn_list = []
    delay_list = []
    for i in range(n):
        delayed = task_wait_random(max_delay)
        delayed.add_done_callback(lambda x: delay_list.append(x.result()))
        spawn_list.append(delayed_task)

    for spawn in spawn_list:
        await spawn

    return delay_list