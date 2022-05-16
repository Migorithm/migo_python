import asyncio , time

async def main():
    print(f"{time.ctime()} Hello!")
    await asyncio.sleep(1.0)
    print(f"{time.ctime()} Goodbye!")

loop = asyncio.get_event_loop()  # Create eventloop instance
task = loop.create_task(main())  # schedules your coroutine to be run on the loop.
loop.run_until_complete(task)    # block the current thread

pending = asyncio.all_tasks(loop=loop) #Return a set of not yet finished Task objects run by the loop.
for task in pending: #gather still pending tasks 
    task.cancel()    # and cancel them 

group = asyncio.gather(*pending,return_exceptions=True) #method for gathering 
loop.run_until_complete(group)   #run them again 

loop.close()                     # It must be called and it will clear all queues and shutdown executor
