from functools import wraps, partial

z = 10


def log(f, x, y):
    print(f.__name__, x, y)
    return f(x, y)  # 'f' is some object implementing __call__ method taking arg x and y


def log_dec(f):
    def log(x, y):
        rv = f(x, y)
        print(f.__name__, x, y, '->', rv)
        return rv

    return log


def add(x, y=10):
    ''' Add two integers '''
    return x + y


@log_dec
def add_with_dec(x, y=10):
    ''' Add two integers '''
    return x + y


# python -i decorators.py   [Interact with all the things script has created]
# >>> z
# 10
# >>> add                    [add is an object]
# <function add at 0x10b194230>
# >>> add.__code__
# <code object add at 0x10e55a3b0, file "decorators.py", line 4>
# >>> add.__defaults__
# (10,)
# >>> add.__doc__
# ' Add two integers '
# >>> add.__name__
# 'add'

sub = add
# >>> sub
# <function add at 0x10b194230>
# >>> sub.__code__
# <code object add at 0x10e55a3b0, file "decorators.py", line 4>
# >>> sub.__defaults__
# (10,)
# >>> sub.__doc__
# ' Add two integers '
# >>> sub.__name__
# 'add'

add.__call__(2, 3)
# 5

log(add, 10, 20)
# ('add', 10, 20)
# 30


# Logging multiple add statement requires 'log' to be called everytime
print('1+2=', log(add, 1, 2))
print('10+2=', log(add, 10, 2))

add = log_dec(add)
print('1+2=', add(1, 2))
print('10+2=', add(10, 2))
print('add_with_dec', add_with_dec(2, 3))


def debug(func):
    @wraps(func)  # Copies metadata(documentation,name) from 'func' to 'wrapper'
    def wrapper(*args, **kwargs):
        print(func.__qualname__)
        return func(*args, **kwargs)

    return wrapper


def add(a, b):
    return a + b


func = debug(add)
func(4, 5)


# Decorators with args
def debug(func=None, *, prefix=''):
    if func is None:
        return partial(debug, prefix=prefix)

    msg = prefix + func.__qualname__

    @wraps(func)  # Copies metadata(documentation,name) from 'func' to 'wrapper'
    def wrapper(*args, **kwargs):
        print(msg)
        return func(*args, **kwargs)

    return wrapper


def add(a, b):
    return a + b


func = debug(prefix='****')(add)
func(4, 5)


# Class decorator , doesn't work with class and static methods
def debugmethods(cls):
    for name, val in vars(cls).items():
        if callable(val):  # identify callables i.e methods
            setattr(cls, name, debug(val))
    return cls


@debugmethods
class Spam:
    def a(self):
        pass

    def b(self):
        pass
Spam().a()