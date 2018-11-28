# https://dev.to/dawranliou/writing-descriptors-in-python-36

# A descriptor is an object attribute with “binding behavior”,
# one whose attribute access has been overridden by methods in the descriptor protocol.
# Those methods are __get__(), __set__(), and __delete__().
# If any of those methods are defined for an object, it is said to be a descriptor.

# Why descriptors
class Order:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total(self):
        return self.price * self.quantity


apple_order = Order('apple', 1, 10)
print(apple_order.total())

# Bug
apple_order.quantity = -10
print(apple_order.total())


# Instead of using getter and setter methods and break the APIs,
# use property to enforce quantity be positive.
class Order:
    def __init__(self, name, price, quantity):
        self._name = name
        self.price = price  # price attribute cannot be negative neither.
        self._quantity = quantity

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError('Cannot be negative.')
        self._quantity = value

    def total(self):
        return self.price * self.quantity


apple_order = Order('apple', 1, 10)
try:
    apple_order.quantity = -10
except ValueError:
    print("Raised exeception")
print(apple_order.total())


# 'price' attribute cannot be negative neither. It might be attempting to just create another property for price,
# but remember the DRY principle. Also, in our example, there might be more attributes need to be added into this class in the future.


# Use descriptors, How to write descriptors?

# Define the NonNegative class and implement the descriptor protocols.
class NonNegative:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Cannot be negative.')
        instance.__dict__[self.name] = value


class Order:
    price = NonNegative('price')  # Similar to SQLAlchemy
    quantity = NonNegative('quantity')

    def __init__(self, name, price, quantity):
        self._name = name
        self.price = price
        self.quantity = quantity

    def total(self):
        return self.price * self.quantity


apple_order = Order('apple', 1, 10)
apple_order.total()
try:
    apple_order.price = -10
except ValueError:
    print("Raised exeception")

try:
    apple_order.quantity = -10
except ValueError:
    print("Raised exeception")


# In Python 3.6
# object.__set_name__(self, owner, name)
# Called at the time the owning class owner is created. The descriptor has been assigned to name.

class NonNegative:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Cannot be negative.')
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class Order:
    price = NonNegative()
    quantity = NonNegative()

    def __init__(self, name, price, quantity):
        self._name = name
        self.price = price
        self.quantity = quantity

    def total(self):
        return self.price * self.quantity


apple_order = Order('apple', 1, 10)
apple_order.total()

try:
    apple_order.price = -10
except ValueError:
    print("Raised exeception")

try:
    apple_order.quantity = -10
except ValueError:
    print("Raised exeception")
