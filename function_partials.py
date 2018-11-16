from functools import partial

# partial(func, *args, **kwargs)
# Returns a new "partial object" which behaves like func called with args & kwargs
# If more arguments are passed in, they are appended to args
# If more keyword arguments are passed in, they extend and override kwargs


# Binary to Decimal conversion
int('10010', base=2)

# Call above function without passing Base

basetwo = partial(int, base=2)
basetwo('10010')