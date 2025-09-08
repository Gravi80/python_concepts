from dis import dis

"""
From the interpreter's point of view, it doesn't understand the separate steps in our computation.

It only sees a series of byte codes, all blended together without any clear distinctions. 
Because of this, when the Python interpreter runs this script, it executes the whole thing from start to finish. 
It has to do this because it doesn't know where it could stop. 
It just sees byte codes, which might be parts of these steps but aren't clearly marked as separate steps. 
"""


def func(data):
    x = data + 1
    y = data * 2
    z = data ** 3

    return x, y, z


"""
In Python, we can break down large computations into smaller, manageable parts. 
By transforming the original function into a generator, we can yield each intermediate result step by step. 
This way, the interpreter processes each part separately, not just as a single block of code.
"""


def gen(data):
    x = data + 1
    yield x
    y = data * 2
    yield y
    z = data ** 3
    yield z


if __name__ == '__main__':
    dis(func)
    print(f'{func(123) = :}')

    # In the generator version, since the computation is broken down into parts,
    # the Python interpreter allows you to handle each part separately.
    # This gives you the flexibility to choose which parts you want to run.
    '''
        Here’s a clearer explanation:
        
        The Python interpreter executes a sequence of bytecodes until it encounters a `yield` statement. 
        When it hits a `yield`, it pauses and remembers its current state, including:
        
        - The position in the code where it stopped
        - The values of local variables
        - The last instruction it executed
        
        So, when it returns control to the caller, it keeps track of its exact position and state, 
        so it can continue from where it left off when the next value is requested. 
    '''

    dis(gen)
    gi = gen(123)
    print(f'{next(gi) = :>12,} {gi.gi_frame.f_lasti = } {gi.gi_frame.f_locals = }')
    print(f'{next(gi) = :>12,} {gi.gi_frame.f_lasti = } {gi.gi_frame.f_locals = }')
    print(f'{next(gi) = :>12,} {gi.gi_frame.f_lasti = } {gi.gi_frame.f_locals = }')
"""
Bytecode Comparison:

| Line | Original Function                             | Line | Generator Version                           |
|------|------------------------------------------------|------|---------------------------------------------|
| 14   | 0 LOAD_FAST                0 (data)           | 29   | 0 LOAD_FAST                0 (data)         |
|      | 2 LOAD_CONST               1 (1)              |      | 2 LOAD_CONST               1 (1)            |
|      | 4 BINARY_ADD                                    |      | 4 BINARY_ADD                                |
|      | 6 STORE_FAST               1 (x)              |      | 6 STORE_FAST               1 (x)            |
| 15   | 8 LOAD_FAST                0 (data)           | 30   | 8 LOAD_FAST                1 (x)            |
|      | 10 LOAD_CONST               2 (2)             |      | 10 YIELD_VALUE                              |
|      | 12 BINARY_MULTIPLY                               |      | 12 POP_TOP                                  |
|      | 14 STORE_FAST               2 (y)             | 31   | 14 LOAD_FAST                0 (data)        |
| 16   | 16 LOAD_FAST                0 (data)          |      | 16 LOAD_CONST               2 (2)           |
|      | 18 LOAD_CONST               3 (3)             |      | 18 BINARY_MULTIPLY                          |
|      | 20 BINARY_MULTIPLY                               |      | 20 STORE_FAST               2 (y)           |
|      | 22 STORE_FAST               3 (z)             | 32   | 22 LOAD_FAST                2 (y)           |
| 18   | 24 LOAD_FAST                1 (x)             |      | 24 YIELD_VALUE                              |
|      | 26 LOAD_FAST                2 (y)             |      | 26 POP_TOP                                  |
|      | 28 LOAD_FAST                3 (z)             | 33   | 28 LOAD_FAST                0 (data)        |
|      | 30 BUILD_TUPLE              3                  |      | 30 LOAD_CONST               3 (3)           |
|      | 32 RETURN_VALUE                                |      | 32 BINARY_MULTIPLY                          |
|      |                                                |      | 34 STORE_FAST               3 (z)           |
|      |                                                | 34   | 36 LOAD_FAST                3 (z)           |
|      |                                                |      | 38 YIELD_VALUE                              |
|      |                                                |      | 40 POP_TOP                                  |
|      |                                                |      | 42 LOAD_CONST               0 (None)        |
|      |                                                |      | 44 RETURN_VALUE                             |
"""
