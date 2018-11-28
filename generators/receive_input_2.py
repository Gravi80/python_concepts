# Use yield to receive a value
def receiver():
    index = 0
    while True:
        print(f"{index}_before yield")
        item = yield
        print(f"{index}_after yield")
        print(f'{index}_Got', item)
        index = index + 1


recv = receiver()
next(recv)  # You can't send() a value the first time because the generator did not execute until
# the point where you have the yield statement so there is nothing to do with the value.
# Calling next on your object will start the generator[move the generator
recv.send("Hello")
recv.send("World")
