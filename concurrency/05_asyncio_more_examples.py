import asyncio


async def main():
    print('tim')
    await foo('text')  # foo('text') creates a Coroutine
    # whereas await executes the Coroutine
    print('finished')


async def foo(text):
    print(text)
    await asyncio.sleep(1)


asyncio.run(main())
# The above code is still synchronous. We are awaiting "foo('text')" to happen and then
# I print finished.
# But if "await asyncio.sleep(1)" is doing no CPU operations then we should be able to do
# something else.
# Ideally when "await asyncio.sleep(1)" is sleeping(waiting for something to happen)
# we actually want to run the next line of code "print('finished')".
# "print('finished')" should not be blocked by "await foo('text')"
print("*********************************************************************")


# asyncio tasks

async def main():
    print('tim')
    task = asyncio.create_task(foo('text'))  # Start executing "foo('text')" as soon as
    # possibly it can and then to allow other code to run while this task is not running/waiting
    print('finished')


asyncio.run(main())

print("*********************************************************************")


# If I want this task to finish first(wait for the task to finish) before we ran "print('finished')".
# We have to await the task

async def main():
    print('tim')
    task = asyncio.create_task(foo('text'))
    await task  # wait until this task is finished
    print('finished')


asyncio.run(main())

print("*********************************************************************")


# Futures
# We want to get the value from fetch_data

async def fetch_data():
    print('start fetching')
    await asyncio.sleep(2)
    print('done fetching')
    return {'data': 1}


async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)


async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())

    # If you want to get the value returned from a coroutine you must await that coroutine/task
    value = await task1
    print(value)
    await task2


asyncio.run(main())
