import collections.abc


class ParentClass:
    pass


# Child class knows about the ParentClass. ParentClass doesn't know ChildClass
class ChildClass(ParentClass):
    pass


# [Virtual Subclass]
# ParentClass knows child class but ChildClass doesn't know ParentClass
# ParentClass.register(ChildClass)
collections.abc.Sequence.register(tuple)
collections.abc.Sequence.register(str)
collections.abc.Sequence.register(range)
collections.abc.MutableSequence.register(list)

# Classes that can register other classes are called Abstract base classes
# ABCs are categories/labels/tags. It's a way to say this class behaves like something.
# But it's a promise. I am tagging my class as a sequence/mutableSequence etc.

# Registering is a promise, there is check happens while registering
import collections


class MyClass:
    pass


issubclass(MyClass, collections.abc.Sequence)  # False
collections.abc.Sequence.register(MyClass)  # No type check happens to see if Myclass is really a sequence
issubclass(MyClass, collections.abc.Sequence)  # True

# Custom Abstract base classes
from abc import ABCMeta


class MyAbc(metaclass=ABCMeta):
    pass


MyAbc.register(tuple)

assert issubclass(tuple, MyAbc)
assert isinstance((), MyAbc)


class AnswerType(type):
    def __init__(self, name, bases, namespace):
        self.answer = 42

    def __new__(metacls, name, bases, namespace, **kwds):
        result = type.__new__(metacls, name, bases, dict(namespace))
        import pdb; pdb.set_trace()
        result._filters = [
            value for value in namespace.values() if hasattr(value, '_filter')]
        return result


class Book(metaclass=AnswerType):
    pass
