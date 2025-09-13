import time
from scalene import scalene_profiler
@profile
def consume_memory(size_in_mb):
    # Allocate a list to consume memory (1 int ~ 24 bytes in CPython)
    num_ints = (size_in_mb * 1024 * 1024) // 24
    data = [0] * num_ints
    return data

@profile
def consume_cpu(duration_sec):
    # Perform CPU-intensive calculations for a given duration
    end_time = time.time() + duration_sec
    x = 0
    while time.time() < end_time:
        x += sum(i * i for i in range(1000))
    return x


if __name__ == "__main__":
    scalene_profiler.start()
    print("Consuming memory...")
    mem = consume_memory(1000)  # 200 MB
    print("Consuming CPU...")
    result = consume_cpu(200)  # 10 seconds
    print("Done.")
    scalene_profiler.stop()
