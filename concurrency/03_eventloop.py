# Eventloop
    # The Event loop is a very efficient task manager
    # They coordinate tasks
    # Run asynchronous tasks and callbacks

import asyncio

async def data_reply():
    await asyncio.sleep(2)
    return {"data":100}

async def file_reply():
    await asyncio.sleep(4)
    return "File returned"

async def task1():
    print("Waiting for data...")
    x = await data_reply()
    print(x)

async def task2():
    print("Waiting for file...")
    x = await file_reply()
    print(x)

async def main():
    
    #asyncio.create_task(task1())
    #asyncio.create_task(task2())
    #without wait, "Waiting for xxx" will be fired off 
    #But it's not going to wait for reply at all
    #using await below will ensure we are waiting for reply. 
    
    x= asyncio.create_task(task1())
    y= asyncio.create_task(task2())
    await x
    await y

asyncio.run(main())
    