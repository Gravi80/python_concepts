import numpy as np

# Array arithmetic
x = np.arange(4)
print("x     =", x)
print("x + 5 =", x + 5)  # np.add
print("x - 5 =", x - 5)  # np.subtract
print("x * 2 =", x * 2)  # np.multiply
print("x / 2 =", x / 2)  # np.divide
print("x // 2 =", x // 2)  # np.floor_divide
print("-x     = ", -x)  # np.negative
print("x ** 2 = ", x ** 2)  # np.power
print("x % 2  = ", x % 2)  # np.mod

# For all ufuncs, you can specify the output variable
y = np.empty(4)
np.multiply(x, 10, out=y)
print(y)

y = np.zeros(4)
np.power(2, x, out=y)
print(y[::2])

# somesequence[::3]
# it means 'nothing for the first argument, nothing for the second, and jump by three'.
# It gets every third item of the sequence sliced.
