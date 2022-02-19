import asyncio

async def main():
    print('tim')
    task = asyncio.create_task(foo("text"))
    await asyncio.sleep(0.5)
    print("finished")

# asyncio.run creates event loop and

async def foo(text):
    print(text)
    await asyncio.sleep(10)
    print(text,text)
#await keyword is allowed only inside async function. 

asyncio.run(main())



#https://www.youtube.com/watch?v=t5Bo1Je9EmE