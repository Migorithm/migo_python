# Create 3 coroutines names t1,t2,t3.
# Each coroutine should print out the name of the coroutine
# Call/run the first coroutine and using await have t2 print out first, 
# t1 print out second and t3 print out last. 

import asyncio

async def t1():
    await asyncio.sleep(2)
    print("t1")

async def t2():
    await asyncio.sleep(1)
    print("t2")

async def t3():
    await asyncio.sleep(3)
    print("t3")

async def main():
    x = asyncio.create_task(t1())
    y = asyncio.create_task(t2())
    z = asyncio.create_task(t3())
    await x
    await y
    await z

asyncio.run(main())