A ufunc in numpy is a Universal Function also known as a vectorized operation.
This is a function operates element-wise on an ndarrays supporting array broadcasting, type casting, and several other standard features.

Many of the built-in functions are implemented in compiled C code,
but **ufunc** instances can also be produced using the **frompyfunc** factory function.

Numpy UFuncs are faster than Python functions involving loops, because the looping happens in compiled code. This is only possible when types are known beforehand, which is why numpy arrays must be typed.

Ufuncs exist in two flavors: unary ufuncs, which operate on a single input, and binary ufuncs, which operate on two inputs.


NumPy has many more ufuncs available, including hyperbolic trig functions, bitwise arithmetic, comparison operators,
conversions from radians to degrees, rounding and remainders, and much more.
A look through the NumPy documentation reveals a lot of interesting functionality.