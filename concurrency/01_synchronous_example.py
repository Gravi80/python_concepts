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


# Multiple requests one by one
@timer(1, 1)
def main():
    with requests.Session() as session:
        for _ in range(100):
            fetch(session, URL)
