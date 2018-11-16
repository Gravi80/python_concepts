# Signature.bind call. Holds the mapping of arguments to the function's parameters.
# Creates a mapping from positional and keyword arguments to parameters.
from inspect import signature


def foo(a, b):
    print(f"{a}+{b}={(a + b)}")


import inspect

print(inspect.signature(foo))

sig = signature(foo)

bound = sig.bind(5, 4)
print(bound.args)
print(bound.kwargs)
print(bound.arguments)
foo(*bound.args, **bound.kwargs)

bound = sig.bind(5)
print(bound.args)
print(bound.kwargs)
print(bound.arguments)
foo(*bound.args, **bound.kwargs)
