from types import new_class

print("Provides utility function to dynamically create new types.")

print("\n**************Create a class object dynamically**************")


def callback(class_namespace):
    print(class_namespace)
    class_namespace['var1'] = 'var1_value'


class BaseMeta(type):
    def __new__(cls, name, bases, body, some_arg):
        print(f"received some_args={some_arg}")
        return super().__new__(cls, name, bases, body)


# kwds : class keyword arguments, These meta-arguments are useful when configuring meta-classes.
ClassA = new_class('ClassA', (object,), {'metaclass': BaseMeta, 'some_arg': 'value'}, callback)
print(ClassA.var1)

print("\n***********************A read-only dict************************")
from types import MappingProxyType

data = {'a': 1, 'b': 2}
read_only = MappingProxyType(data)
print(read_only)
try:
    read_only['a'] = 3
except TypeError:
    print("can't modify read only")

# read_only is actually a view of the underlying dict(data), and is not an independent object.
data['a'] = 3
data['c'] = 4
print(read_only)

print("\n***********************Class allowing you to set, change and delete attributes.************************")
from types import SimpleNamespace

dict_data = {'c': 3, 'd': 4}
data = SimpleNamespace(a=1, b=2, **dict_data)
print(data)
data.e = 5
print(data)
print("data.c=", data.c)
