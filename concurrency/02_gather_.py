import asyncio
import time

async def count():
    await asyncio.sleep(1) #Task can release its CPU when they are in waiting period
    print("1")             # So the other task can use CPU time.
    await asyncio.sleep(1)
    print("2")
    await asyncio.sleep(1)
    print("3")
    
async def main():
    await asyncio.gather(count(),count(),count())


if __name__ =="__main__":
    t = time.perf_counter()
    asyncio.run(main())
    t2 = time.perf_counter()
    print(f"Total time elapsed: {t2-t} seconds")
    
