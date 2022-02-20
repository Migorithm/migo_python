import asyncio

async def task1():
    print("Send first email")
    asyncio.create_task(task2())
    await asyncio.sleep(5)
    print("First Email reply")

async def task2():
    print("Send second email")
    asyncio.create_task(task3())
    await asyncio.sleep(2)
    print("Second Email reply")

async def task3():
    print("Send third email")
    await asyncio.sleep(1)
    print("third Email reply")

asyncio.run(task1())