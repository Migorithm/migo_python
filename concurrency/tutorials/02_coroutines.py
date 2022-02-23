#Coroutines
    # Asynchronous function in Python is typically called coroutines
    # Coroutines declaed with the async/await syntax
    # Coroutines are special functions that return coroutine objects when called.

import asyncio

#Create Asynchronous coroutine
async def send_email():
    print("hello")

# We need this asyncio.run because coroutine function returns 
# coroutine object as described and this is the way to run that object. 
asyncio.run(send_email())


async def send_email2():
    print("hello2")

    #We will wait for this task to complete
    # sleep is what provides us a way of simulating delay. 
    await asyncio.sleep(2)
    print("Awake now")

asyncio.run(send_email2())


async def t1():
    await t2()
    print("t1")
async def t2():
    await t3()
    print("t2")
async def t3():
    print("t3")
asyncio.run(t1())



async def data_reply():
    await asyncio.sleep(4)
    return {"data":100}


async def file_reply():
    await asyncio.sleep(2)
    return ("file returned")
    

async def task1():
    print("Waiting for data...")
    #while we are waiting we could have another task
    x = await data_reply()
    print(x)

async def task2():
    print("Waiting for file...")
    #while we are waiting we could have another task
    x = await file_reply()
    print(x)

#Event loop
async def main():
    x = asyncio.create_task(task1())
    y = asyncio.create_task(task2())
    await x
    await y

    
asyncio.run(main())

