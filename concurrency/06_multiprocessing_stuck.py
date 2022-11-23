# ********* Multiprocessing gets stuck when one of the child process is killed ********
import os
import random
from multiprocessing import Pool


def some_processing(*args):
    print(f"{os.getpid()}=start processing")
    if random.randint(0, 10) % 2 == 0:
        print(f"Kill {os.getpid()}")
        # os.kill(os.getpid(), 9)
        # exit()
        quit()
    else:
        print(f"{os.getpid()}=finish processing")
    return "Hello"


result_list = []


def log_result(result):
    # This is called whenever some_processing() returns a result.
    # result_list is modified only by the main process, not the pool workers.
    result_list.append(result)


if __name__ == '__main__':
    pool = Pool(processes=4)
    [pool.apply_async(some_processing, (), callback=log_result) for i in range(1)]
    # [pool.apply(some_processing, ()) for i in range(1)]
    # pool.map(some_processing, range(1))
    pool.close()
    pool.join()
    # print([f"*****{os.getpid()}={res.get()}" for res in multiple_results])
    print([f"*****{os.getpid()}={result_list}"])
