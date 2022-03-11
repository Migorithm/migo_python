import asyncio

"""
scheduler is another name of eventloop.
eventloop keeps track of all the running task and 
when a function is suspended, it gives control back to 
eventloop, which will then find another function to start or resume.

asyncio provides framework. 
"""

loop = asyncio.get_event_loop()

async def greeter(name):
    print("Hi "+ name +", you are in a coroutine")
    
try:
    print("starting coroutine")
    coro = greeter("LP")
    print("Entering event loop")
    loop.run_until_complete(coro)
finally:
    print("closing event loop")
    loop.close()
    
"""
An Application that interacts with eventloop explicitly registers code 
to be run and lets eventloop( scheduler) make the necessary calls 
into application code when resources are available. 
"""