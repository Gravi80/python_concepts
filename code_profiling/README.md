### Standard system utility on Unix-like systems
`/usr/bin/time -p python <python_script>.py`

* "real" records the wall clock or elapsed time.
* "user" records the amount of time the CPU spent on your task outside of kernel functions.
* "sys" records the time spent in kernel-level functions.

By adding "user" and "sys", you get a sense of how much time was spent in the CPU. 
The difference between this and real might tell you about the amount of time spent waiting for I/O

We can add the --verbose flag to get even more output.

* One useful indicator is Maximum resident set size, which indicates the maximum amount of RAM used during execution
* Another useful indicator here is Major (requiring I/O) page faults. This indicates whether the operating system is having to load pages of data from the disk because the data no longer resides in RAM, which will cause a speed penalty; here it doesn’t, as it records zero page faults.

### cProfile is a built-in profiling tool in the standard library.

`python -m cProfile -s cumulative <python_script>.py`

* -s cumulative flag tells cProfile to sort by cumulative time spent inside each function; this gives us a view into the slowest parts of a section of code.

To get more control over the results of cProfile, we can write a statistics file and then analyze it in Python:

`python -m cProfile -o profile.stats <python_script>.py`

We can load this into Python as follows, and it will give us the same cumulative time report as before:
```python
import pstats
p = pstats.Stats('profile.stats')
p.sort_stats('cumulative').print_stats(10)  # print top 10 functions
p.print_callers()  # print functions that called the listed functions
p.print_callees() # print functions that were called by the listed functions
```

#### Visualizing cProfile Output with SnakeViz
`pip install snakeviz`

### Using line_profiler for Line-by-Line Measurements
line_profiler is the strongest tool for identifying the cause of CPU-bound problems in Python code.
you should start with cProfile and use the high-level view to guide which functions to profile with line_profiler.
`pip install line_profiler`

A decorator (@profile) is used to mark the chosen function.

The `kernprof` script is used to execute your code, and the CPU time and other statistics for each line of the chosen function are recorded.

`kernprof -l -v <python_script>.py`

* -l for line-by-line (rather than function-level) profiling
* -v for verbose output.


### Using memory_profiler to Diagnose Memory Usage
line_profiler package measures CPU usage, the memory_profiler measures memory usage on a line-by-line basis.

* memory_profiler operates in a very similar way to line_profiler but runs far more slowly. If you install the `psutil` package (optional but recommended), memory_profiler will run faster.

`pip install memory_profiler psutil`

`python -m memory_profiler <python_script>.py`

* memory_profiler has a utility called mprof, used once to sample the memory usage and a second time to visualize the samples. It samples by time and not by line, so it barely impacts the runtime of the code.

`mprof run <python_script>.py`
* This writes a statistics file that is then visualized using mprof plot

### Combining CPU and Memory Profiling with Scalene
Scalene combines CPU, memory profiling, and GPU profiling into one easy-to-run package.
`pip install scalene`
`scalene <python_script>.py`

* It has options to restrict profiling with an @profile decorator (similar to line_profiler and memory_profiler) and to filter in or out certain filenames
 

### Introspecting an Existing Process with PySpy
`pip install py-spy`

* It introspects an already-running Python process and reports in the console with a top-like display.
* If your process is already running, you’ll want to use ps to get its process identifier (the PID); then this can be passed into `py-spy`.
* py-spy needs sudo privileges, which would run it in the superuser’s environment, so we pass in our login’s PATH using sudo env "PATH=$PATH" when calling py-spy along with the process identifier to monitor.

#### Running PySpy at the command line
```bash
ps -A -o pid,rss,cmd | ack python
...
95671 94984 python julia1_nopil.py
...
sudo env "PATH=$PATH" py-spy top --pid 95671
```


#### PySpy can also export a flame chart, we’ll run that option while asking PySpy to run our code directly without requiring a PID using
`py-spy record -o profile.svg —python <python_script>.py`

### Probing how well memory is being moved to the CPU can be quite hard 

However, in Linux the `perf tool` can be used to get amazing amounts of insight into how the CPU is dealing with the program being run.
```bash
perf list
```

```bash
perf stat -e cycles,instructions,\
    cache-references,cache-misses,branches,branch-misses,task-clock,faults,\
    minor-faults,cs,migrations python <python_script>.py
```
1. task-clock: how many clock cycles our task took. This is different from the total runtime, because if our program took one second to run but used two CPUs, then task-clock would be 2000 (task-clock is generally in milliseconds).
2. instructions: tells us how many CPU instructions our code issued
3. cycles: tells us how many CPU cycles it took to run all of these instructions. The difference between these two numbers gives us an indication of how well our code is vectorizing and pipelining. With pipelining, the CPU is able to run the current operation while fetching and preparing the next one.
4. cs(“context switches”) and migrations: tell us about how the program is halted in order to wait for a kernel operation to finish (such as I/O), to let other applications run, or to move execution to another CPU core.
   When a context-switch happens, the program’s execution is halted and another program is allowed to run instead.
   migrations happen when the program is halted and resumed on a different CPU than the one it was on before, in order to have all CPUs have the same level of utilization. This can be seen as an especially bad context switch, as not only is our program being temporarily halted, but we also lose whatever data we had in the L1 cache (recall that each CPU has its own L1 cache).
5. page-faults(fault): When memory is allocated, the kernel doesn’t do much except give the program a reference to memory. Later, however, when the memory is first used, the operating system throws a minor page fault interrupt, which pauses the program that is being run and properly allocates the memory. This is called a lazy allocation system.
   There is also a major page fault, which happens when the program requests data from a device (disk, network, etc.) that hasn’t been read yet. These are even more expensive operations: not only do they interrupt your program, but they also involve reading from whichever device the data lives on. This sort of page fault does not generally affect CPU-bound work; however, it will be a source of pain for any program that does disk or network reads/writes.
6. cache-references: Once we have data in memory and we reference it, the data makes its way through the various tiers of memory (L1/L2/L3 memory) Whenever we reference data that is in our cache, the cache-references metric increases.
7. cache-miss: If we do not already have this data in the cache and need to fetch it from RAM, this counts as a cache-miss.
8. branch: A branch is a time in the code where the execution flow changes. This is essentially a branch in the execution of the code—the next instruction in the program could be one of two things.
   To optimize this, especially with regard to the pipeline, the CPU tries to guess which direction the branch will take and preload the relevant instructions. When this prediction is incorrect, we will get a branch-miss. 

### A better tool is asizeof in pympler
```python
from pympler.asizeof import asizeof
asizeof([x for x in range(int(1e7))])
%memit [x for x in range(int(1e7))] # We prefer to use memit, as it gives us an accurate count of memory usage on the machine in question.
```
