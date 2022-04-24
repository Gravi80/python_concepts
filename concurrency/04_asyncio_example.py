# Just like multithreading also does context-switching to support concurrency.
# It is different then multithreading as
# 1. It uses single thread
# 2. The code decides when to leave control of the running Thread so that
# the other portion of the code could run during the meantime.
# This is unlike multithreading where it is done preemptively by the library itself.
import asyncio

import aiohttp
import timeit
from concurrent.futures import ThreadPoolExecutor

# Gives a new uuid on every request
URL = "https://httpbin.org/uuid"


# How much time it takes to run the complete task
def timer(number, repeat):
    # repeat: Specifies the number of samples to take.
    # number: Specifies the number of times to repeat the code for each sample.

    def wrapper(func):
        runs = timeit.repeat(func, number=number, repeat=repeat)
        print(f"{sum(runs) / len(runs)} seconds")  # Avg. time

    return wrapper


# Coroutine
# The await lets the Coroutine wait for the result of the expression and during that time
# some other Coroutine can run.
async def fetch(session, url):
    async with session.get(url) as response:
        json_response = await response.json()  # response.json() creates a Coroutine
        # whereas await executes the Coroutine
        print(json_response['uuid'])


# Make main a Coroutine
async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, URL) for _ in range(100)]  # create a list of coroutines
        await asyncio.gather(*tasks)  # Allows you to gather a bunch of coroutines
        # and then execute them together.


@timer(1, 5)
def func():
    asyncio.run(main())  # run this coroutine
