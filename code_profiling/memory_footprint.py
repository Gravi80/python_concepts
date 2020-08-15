import psutil, os


def memory_footprint():
    """Returns memory (in MB) used py python process"""
    mem = psutil.Process(os.getpid()).memory_info().rss
    return mem / 1024 ** 2


print(memory_footprint())
