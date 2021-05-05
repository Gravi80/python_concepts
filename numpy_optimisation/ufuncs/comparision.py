import numpy as np

x = np.arange(4)
print("x < 3 =", x < 3)  # np.less
print("x > 3 =", x > 3)  # np.greater
print("x <= 3 =", x <= 3)  # np.less_equal
print("x >= 3 =", x >= 3)  # np.greater_equal
print("x != 3 =", x != 3)  # np.not_equal
print("x == 3 =", x == 3)  # np.equal
print("(2 * x) == (x ** 2) =",
      (2 * x) == (x ** 2))  # It is also possible to do an element-wise comparison of two arrays,
# and to include compound expressions:


print("All=", np.all(x < 4))  # axis=1 => Row
print("Any=", np.any(x < 4))
