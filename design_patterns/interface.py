from abc import ABCMeta, abstractmethod


class SomeInterface(metaclass=ABCMeta):

    @abstractmethod
    def some_method(self):
        pass


class MyClass(SomeInterface):
    def some_method(self):
        pass


mc = MyClass()
