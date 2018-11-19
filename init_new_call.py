class Demo:
    def __new__(cls, *args, **kwargs):
        print("new")
        instance = super(Demo, cls).__new__(cls, *args, **kwargs)
        return instance

    def __init__(self):
        print("init")

    def __call__(self, *args, **kwargs):
        print("call")


demo = Demo()
demo()

# 1).new
# 2).init
# 3).call

print(callable(demo))
