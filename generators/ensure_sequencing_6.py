# We an API(Task) which provides 3 methods
# indicating the order in which we need to run these functions.

# We we are using this API we want to have some custom code after each task.
# If we wanted to run these method all @ the same time, the API would have never
# provided us 3 methods i.e if we didn't have to have some code between these 3 method,
# they would never be 3 different methods and can be done by 1 method
# def doit():
#     print("First task executed")
#     print("Second task executed")
#     print("Third task executed")

class Task:
    def first(self):
        print("First task executed")

    def second(self):
        print("Second task executed")

    def third(self):
        print("Third task executed")


# With generators you can create code that can interleave with other code and
# also enforces sequencing
def task():
    print("First task executed")
    yield
    print("Second task executed")
    yield
    print("Third task executed")
    yield


if __name__ == '__main__':
    # Nothing stops you from doing this
    Task().third()
    Task().second()
    Task().first()

    task_gen = task()
    next(task_gen)
    print("***** Custom code after first task executed ****")
    next(task_gen)
    print("***** Custom code after second task executed ****")
    next(task_gen)
    print("***** Custom code after third task executed ****")
