class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    # In order to be iterable, a class needs to implement __iter__()
    # __iter__() must return an iterator [Python iterator object must implement two special methods, __iter__() and __next__(),
    #  collectively called the iterator protocol]
    def __iter__(self):
        # can return self, because __next__ implemented
        return self

    # returns an iterator for the given object (array, set, tuple etc. or custom objects).
    # It creates an object that can be accessed one element at a time using __next__() function

    # implement __next__() which must raise StopIteration when there are no more items to return
    def __next__(self):  # Python 3: def __next__(self)
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


for c in Counter(3, 8):
    print(c)


class Fib:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib


for n in Fib(1000):
    print(n, end=' ')


##########################################################
# If iterator doesn't need to maintain state, use generator

class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        while self.current <= self.high:
            yield self.current
            self.current += 1