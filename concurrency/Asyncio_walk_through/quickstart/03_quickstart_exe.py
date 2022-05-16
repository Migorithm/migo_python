import time
import asyncio

async def main():
    print(f"{time.ctime()} Hello!")
    await asyncio.sleep(1.0)
    print(f"{time.ctime()} Goodbye!")
    
def blocking():
    time.sleep(0.5)
    print(f"{time.ctime()} Hello from a thread!")

loop = asyncio.get_event_loop()
task = loop.create_task(main())
loop.run_in_executor(None, blocking) #run in a separate thread. First parameter is type of executure. Passing in 'None' means using the default executor.
loop.run_until_complete(task)

pending= asyncio.all_tasks(loop=loop)
for task in pending:
    task.cancel()

group= asyncio.gather(*pending, return_exceptions=True)
loop.run_until_complete(group)
loop.close()


"""
run_in_executor() does not block the main thread: it only schedules the executor task to run.
As this returns a 'Future' object, you can await it if it is called within another coroutine function.

"""