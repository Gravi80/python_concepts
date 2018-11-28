def func():
    print("Before yield")
    result = yield 2
    print("After yield")
    print("Got:", result)


# creates the generator object. The code is paused at the very top of the function, nothing is executed.
gen = func()

# You either call next(gen) or gen.send(None); the generator commences and executes until the first yield expression:
# and execution now pauses.
# The next(gen) or gen.send(None) calls now return 2, the value yielded by yield 2.
res = gen.send(None)
print(res)

# Because the generator is now paused, the result = ... assignment can't yet take place!
# That'll only happen when the generator is resumed again
try:
    gen.send("some string")
except StopIteration:
    pass
    # The generator function is resumed now:
    # result = <return value of the yield expression>  # 'some string' in this case
    # print("Got:",result)
    # and now the function ends, so StopIteration is raised.


def whizbang():
    for i in range(10):
        print(f"{i}_before yield")
        x = yield i  # means x = yield send_value and yield i
        print(f"{i}_after yield")
        print('i got {}'.format(x))


whiz = whizbang()
res = next(whiz)
print(res)
print("******************")
res = next(whiz)
print(res)
print("******************")
res = next(whiz)
print(res)
print("******************")
res = whiz.send('yo')
print(res)
