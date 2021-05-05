import numpy as np

# To reduce an array with a particular operation, we can use the reduce method of any ufunc.

x = np.arange(1, 6)
print("x=", x)
print(np.add.reduce(x))

# If we'd like to store all the intermediate results of the computation, we can instead use accumulate
print(np.add.accumulate(x))
