# Any function in python with a yield statement is a generator function.
# If a function contains at least one yield statement (it may contain other yield or return statements),
# it becomes a generator function.
# Both yield and return will return some value from a function.
# The difference is that, while a return statement terminates a function entirely,
# yield statement pauses the function saving all its states and later continues from there
# on successive calls.

def my_gen():
    n = 1
    print('This is printed first')
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


gen = my_gen()
next(gen)
next(gen)
next(gen)


def countdown(n):
    print("begin")
    while n > 0:
        print("before yield", n)
        yield n
        print("after yield", n)
        n -= 1


countd = countdown(3)
for n in countd:
    print(n)
