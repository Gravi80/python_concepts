# any ufunc can compute the output of all pairs of two different inputs using the outer method.
import numpy as np

x = np.arange(1, 6)
print(x)
print(np.multiply.outer(x, x))

# ufunc.at and ufunc.reduceat
