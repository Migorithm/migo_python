from fastapi import FastAPI
import asyncio
import uvicorn

app = FastAPI()

@app.get("/")
async def index():
    task1 = asyncio.create_task(async_call())
    task2 = asyncio.create_task(async_call2())
    lst = []
    # asyncio.as_completed is a generator that yields coroutines that retun the results of the coroutine passed to it 
    # IN THE ORDER they are completed
    for res in asyncio.as_completed([task1,task2]): 
        result = await res   #await expression will not blcok but we still need it to get the result from coroutine.
        lst.append(result)
    return lst

async def async_call():
    await asyncio.sleep(5)
    return "Hey!"
    
async def async_call2():
    await asyncio.sleep(3)
    return "It's me!"
    

if __name__ == "__main__":
    uvicorn.run(app, port=8000)