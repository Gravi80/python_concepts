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
