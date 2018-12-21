# __getattribute__ can only be used with new-style classes.
#                   When python looks up attributes on instances,
#                   __getattribute__ is the main entry for all attribute access.
#                    object provides the default implementation.
#                    raise AttributeError, causing __getattr__ to be called.
#
# __get__     Define behavior for when the descriptor's value is retrieved.
# __set__     Define behavior for when the descriptor's value is changed
# __getattr__ Called only when an attribute lookup has not found the attribute in the usual places
#             (i.e. it is not an instance attribute nor is it found in the class tree for self).

class BaseMeta(type):
    def __new__(cls, name, bases, body):
        return super().__new__(cls, name, bases, body)

    def __getattribute__(self, item):
        print("metaclass getattribute", item)
        return super().__getattribute__(item)

    def __setattr__(self, key, value):
        print("metaclass setattr", key, value)
        super().__setattr__(key, value)


class MyClass(object, metaclass=BaseMeta):
    ClassVar = 'ClassVar_initial'

    def __init__(self):
        self.var1 = 'var1_initial'
        self.var2 = 'var2_initial'

    def __setattr__(self, key, value):
        print("set_attr ", key, value)
        self.__dict__[key] = value

    def __getattr__(self, item):
        print("get_attr ", item)

    def __getattribute__(self, item):
        if item != '__dict__':
            print("getattribute", item)
        return super().__getattribute__(item)


instance = MyClass()
instance.var1 = 'foo'  # translates to MyClass.__setattr__
instance.var3 = 'bar'  # translates to MyClass.__setattr__
instance.random_var  # translates to MyClass.__getattribute__ and then MyClass.__get_attr__
instance.var1  # translates to MyClass.__getattribute__
MyClass.ClassVar = "class var"  # translates to BaseMeta.__setattr__
MyClass.ClassVar  # translates to BaseMeta.__getattribute__
