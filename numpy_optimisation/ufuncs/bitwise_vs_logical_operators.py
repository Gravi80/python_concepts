# (and, or) gauge the truth or falsehood of entire object, while
# (&, |) refer to bits within each object.
import numpy as np

print(bool(42), bool(0))
print("bool(42 and 0)=", bool(42 and 0))
print("bool(42 or 0)=", bool(42 or 0))

# (&, |), the expression operates on the bits of the element
print("binary(42)=", bin(42))
print("binary(59)=", bin(59))
print("bin(42 & 59)=", bin(42 & 59))
print("bin(42 | 59)=", bin(42 | 59))

# When you have an array of Boolean values in NumPy, this can be thought of as a string of bits where
# 1 = True and 0 = False, and the result of & and | operates similarly to above:
A = np.array([1, 0, 1, 0, 1, 0], dtype=bool)
B = np.array([1, 1, 1, 0, 1, 1], dtype=bool)
print(A | B)

# Using or on these arrays will try to evaluate the truth or falsehood of the entire array object,
# which is not a well-defined value:
print(A or B)
