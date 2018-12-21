# Step 1

body = '''def __init__(self,name):
    self.name = name
def bar(self):
    print(f"I am {self.name}")'''

# Step 2, create an empty class dictionary
clsdict = type.__prepare__('ClassName', (object,))
print(clsdict)
# Step 3, clsdict is populated with the body methods and attributes
exec(body, globals(), clsdict)
print(clsdict)
# Step 4, Class is constructed
ClassName = type('ClassName', (object,), clsdict)
cn = ClassName('some_name')
cn.bar()


# What if you want to use something other than type in Step 4
# You can specify this by providing metaclass in class definition
class A(metaclass=type):  # Metaclass will be used to construct the class.

    @classmethod
    def __prepare__(metacls, name, bases):
        return {}  # creates and returns dictionary to use for execution of the class body
        # return OrderedDict()

    def my_func(self):
        """Body"""
        pass


# For constructing your own metaclass. Inherit from 'type' and redefine __new__ or __init__
# In meta class if you want to control the initialisation of the class : __new__
# Modify the class by modifying some class attribute : Override __new__
# Check something after initialisation : __init__
# When you want to just carry out checks: Override __init__
class mytype(type):
    def __new__(cls, name, bases, clsdict):
        clsobj = super().__new__(name, bases, clsdict)
        return clsobj


class A(object):

    def my_func(self):
        """Body"""
        pass


# We can also use 'type' to create new class
def my_func(self):
    """Body"""
    pass


class_name = 'A'
super_class = (object,)
methods = {'my_func': my_func}

A = type(class_name, super_class, methods)


def copy_function(f):
    functype = type(f)
    new_func = functype(
        f.__code__,  # bytecode
        f.__globals__,  # global namespace
        f.__name__,  # function name
        f.__defaults__,  # default keyword argument values
        f.__closure__  # closure variables
    )
    new_func.__doc__ = f.__doc__
    return new_func


def make_class(name, parents, methods):
    for f in methods:
        new_func = copy_function(methods[f])
        new_func.__doc__ = "%s: %s" % (name, methods[f].__doc__)
        methods[f] = new_func
    cls = type(name, parents, methods)
    return cls


B = make_class('B', (object,), {'my_func': my_func})
C = make_class('C', (B,), {'my_func': my_func})

print(A().my_func.__doc__)
print(B().my_func.__doc__)


class BaseMeta(type):
    def __new__(cls, name, bases, body):
        print('__new__', name, bases, body)
        if name is not 'Base':
            if 'bar' not in body:
                raise TypeError()
        return super().__new__(cls, name, bases, body)


# As a library author you need to make sure that derived class should implement bar() method
class Base(metaclass=BaseMeta):
    def foo(self):
        return self.bar()


class Derived(Base):
    def bar(self):
        print("some")


# In meta class if you want to control the initialisation of the class : __new__
# Modify the class by modifying some class attribute : Override __new__
# Check something after initialisation : __init__
# When you want to just carry out checks: Override __init__


# https://www.youtube.com/watch?v=Vjx9okHzaiM


print("\n\n######################__init_subclass__###############################")


# how to let the parent know when it is being subclassed (__init_subclass__)
# how to let a descriptor class know the name of the property it is used for (__set_name__)
class PEP487:
    def __init_subclass__(cls, whom, **kwargs):  # This method is called whenever the containing class is subclassed.
        # cls is then the new subclass.
        super().__init_subclass__(**kwargs)
        cls.hello = lambda: print(f"Hello,{whom}")


class HelloWorld(PEP487, whom="World"):
    pass


HelloWorld.hello()

print("\n\n######################__prepare__###############################")


# Allowing a custom namespace[class method/variable] to be used when creating classes.
class Wrapper(type):
    def wrapper(func):
        def wrapped_func(*args, **kwargs):
            print("*****started wrapped****")
            res = func(*args, **kwargs)
            print("*****finished wrapped****")
            return res

        return wrapped_func

    @classmethod
    def __prepare__(metacls, name, bases, **kwargs):
        return {"wrap": metacls.wrapper, "num1": 10}


class Foo(metaclass=Wrapper):

    @wrap
    def sum(self, num2):
        return self.__class__.num1 + num2


print(Foo().sum(2))