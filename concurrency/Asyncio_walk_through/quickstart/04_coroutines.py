"""
Coroutine internals: using send() and Stopiteration
"""

async def f():
    return 123

coro = f()

try :
    coro.send(None) #1 
except StopIteration as e:
    print("The answer was:", e.value) #2
    


"""
#1 
A coroutine is initiated by "sending" it a None. Internally, 
this is what the event loop is going to be doing to your coroutines;
You will never have to do this manually. All the coroutines you make
will be executed either with loop.create_task(coroutine) or await coroutine. 
It's the loop that does the '.send(None)' behind the scenes.


#2
When the coroutine returns, we can access the return value via value attribute.
"""

import asyncio
async def func():
    await asyncio.sleep(1.0)
    return 123

async def main():
    result = await func() #1
    return result

a = asyncio.run(main())
print(a) #123
"""
#1
Calling func() produces a coroutinel; this means we are allowed to await it.
"""




#Throwing cancellation

# async def m():
#     try:
#         while True: 
#             await asyncio.sleep(0)
#     except asyncio.CancelledError:
#         print("I was cancelled!")


# coro = m()
# coro.send(None)
# coro.send(None)
# coro.throw(asyncio.CancelledError) # "I was cancelled!" will be printed




#Stop predenting to be an event loop by manually doing all the .send(None) calls
async def z():
    await asyncio.sleep(0)
    print("hey!")
    return 111

loop2 = asyncio.get_event_loop()
coro = z()
loop2.run_until_complete(coro)
