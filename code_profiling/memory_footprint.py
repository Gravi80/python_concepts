import os
import psutil
import sys


def memory_footprint():
    """Returns memory (in MB) used py python process"""
    mem = psutil.Process(os.getpid()).memory_info().rss
    # bytes to MB
    return mem / 1024 ** 2


print(f"before={memory_footprint()}")
N = (1024 ** 2) // sys.getsizeof(float())  # Number of floats that fill 1 MB
x = [float(i) for i in range(0, 50 * N)]

print(f"after={memory_footprint()}")
