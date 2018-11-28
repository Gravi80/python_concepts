def double():
    try:
        while True:
            item = yield
            print("Received", item)
            yield 2 * item
            print("Value Returned")
    except GeneratorExit:
        print("Received Closing Generator")


db = double()
res = next(db)
print("*****res=", res)
res = db.send(2)
print("*************************res=", res)
