# Utilise multiple CPU units/cores by spawning multiple processes.
# Each process is independent of each other and can execute parallelly.

# The Pool class represents a pools of workers processes,
# we can automatically distribute the tasks among the workers by using the Pool object.
# The creation of processes and orchestration of tasks will be taken care by Pool.
from multiprocessing import Pool

import requests
import timeit

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


def fetch(session, url):
    with session.get(url) as response:
        print(response.json()['uuid'])


@timer(1, 1)
def main():
    with Pool() as pool:
        with requests.Session() as session:
            pool.starmap(fetch, [(session, URL) for _ in range(100)])

# Overhead of creating new processes and also a portion of work
# is still happening sequentially.
# In each process the requests processing will happen sequentially.
