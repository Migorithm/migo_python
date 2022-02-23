"""
Let's build a coroutine called 'fetch_data' which simulates the
collection of data from a network database. Let's assume that takes
a few seconds. It should return a dictionary {"data":100}. 

Next, build a new coroutine which  counts down from 10 to 1(using range).
Using await, have each number print to the screen every 1 seconds.
Finally build a coroutine called main() and run fetch_data and the 
countdown coroutine concurrently. Print the data that is returned 
from fetch_data whilst also counting down from 10.
"""

import asyncio

async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(5)
    print("Data returned...")
    return {"data":100}

async def countdown():
    for i in range(10,0,-1):
        await asyncio.sleep(1)
        print(i)

async def main():
    x = asyncio.create_task(fetch_data())
    y = asyncio.create_task(countdown())
    
    data = await x
    print(data)
    await y

asyncio.run(main())