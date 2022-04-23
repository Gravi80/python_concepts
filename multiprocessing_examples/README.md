The `multiprocessing` module provides a low-level interface to process and thread-based parallelism:
* Parallelize a CPU-bound task with `Process` or `Pool` objects
  
    `Process`: A forked copy of the current process; this creates a new process identifier, and the task runs as an independent child process in the operating system.
    
     `Pool`: Wraps the `Process` or `threading.Thread` API into a convenient pool of workers that share a chunk of work and return an aggregated result.
  
* Parallelize an I/O-bound task in a `Pool` with threads using the (oddly named) `dummy` module
* Share pickled work via a `Queue`
  
    `Queue`: A FIFO queue allowing multiple producers and consumers.    

* Share state between parallelized workers, including bytes, primitive datatypes, dictionaries, and lists
    
    `Pipe`: A uni- or bidirectional communication channel between two processes.
    
    `Manager`: A high-level managed interface to share Python objects between processes.

    `ctypes`: Allows sharing of primitive datatypes (e.g., integers, floats, and bytes) between processes after they have forked.

Threads in Python are OS-native(actual operating system threads), 
they are bound by the GIL, so only one thread may interact with Python objects at a time.

