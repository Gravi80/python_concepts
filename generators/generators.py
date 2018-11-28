def fib(a=1, b=1, n=10):
    res = []
    for _ in range(n):
        res.append(a)
        a, b = b, a + b
    return res


print(fib())


def fib(a=1, b=1):
    while True:
        yield a
        a, b = b, a + b


from itertools import islice, takewhile, dropwhile

print(list(islice(fib(), 10)))
print(list(takewhile(lambda x: x < 10, fib())))
print(list(dropwhile(lambda x: x < 10, islice(fib(), 10))))

print(list(dropwhile(lambda x: x < 5,
                     takewhile(lambda x: x < 100,
                               islice(fib(), 30)))))
