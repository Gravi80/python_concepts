def chain(x, y):
    yield from x
    yield from y


a = [1, 2, 3]
b = [4, 5, 6]

for n in chain(a, b):
    print(n)


# Behind yield from
def chain1(x, y):
    for n in x:
        yield n
    for n in y:
        yield n


for n in chain1(a, b):
    print(n)

for n in chain(chain(a, b), chain(b, b)):
    print(n)
