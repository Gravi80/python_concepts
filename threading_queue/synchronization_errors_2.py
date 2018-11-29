# Synchronization errors occur when you have two threads accessing a common mutable chunk of data.
# Threaded programming requires that the programmer be very, very mindful of what data needs to be
# shared amongst workers, how to protect (i.e. lock) that data so that you do not run into
# the dreaded race-condition or the even more dreadful Deadlock.
from threading import Thread


class Person(object):
    def __init__(self):
        self._age = 10

    def get_age(self):
        return self._age

    def increment_age(self):
        self._age += 1


def task1(person):
    person.increment_age()
    # sleep(1)
    print("task1 get_age()=", person.get_age())
    print('t1:', person.get_age() == 11)


def task2(person):
    person.increment_age()
    print("task2 get_age()=", person.get_age())
    print('t2:', person.get_age() == 11)


person = Person()
# Create two threads modifying the same ob instance
thread1 = Thread(target=task1, args=(person,))
thread2 = Thread(target=task2, args=(person,))
thread1.start()
thread2.start()
thread1.join()
thread2.join()
