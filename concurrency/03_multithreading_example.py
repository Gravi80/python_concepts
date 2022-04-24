import requests
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


def fetch(session, url):
    with session.get(url) as response:
        print(response.json()['uuid'])


@timer(1, 5)
def main():
    with ThreadPoolExecutor(max_workers=20) as executor:
        with requests.Session() as session:
            executor.map(fetch, [session] * 100, [URL] * 100)
            executor.shutdown(wait=True)
