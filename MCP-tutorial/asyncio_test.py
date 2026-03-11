# import asyncio

# async def func():
#     print("Hello!")
#     await asyncio.sleep(2) #pauses for 2 seconds but without blocking
#     print("Twishanu")

# asyncio.run(func())

import asyncio

async def func1():
    print("Task 1 started")
    await asyncio.sleep(3) #waits for 3 seconds but does not block other async functions
    print("Task 1 finished")

async def func2():
    print("Task 2 started")
    await asyncio.sleep(1)
    print("Task 2 finished") # waits for 1 second in the meantime runs 1 second of task 1

async def main():
    await asyncio.gather(func1(), func2())

asyncio.run(main())

