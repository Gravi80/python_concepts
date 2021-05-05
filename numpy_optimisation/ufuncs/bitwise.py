import numpy as np

x = np.arange(4)
print("Bitwise and", np.sum((x > 1) & (x < 3)))  # np.bitwise_and
print("Bitwise or", np.sum((x > 1) | (x < 3)))  # np.bitwise_or
print("Bitwise xor", np.sum((x > 1) ^ (x < 3)))  # np.bitwise_xor
print("Bitwise not", np.sum(~((x <= 1) | (x >= 3))))  # np.bitwise_not
