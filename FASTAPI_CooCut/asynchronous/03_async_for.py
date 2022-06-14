from fastapi import FastAPI
import asyncio
import uvicorn

app = FastAPI()

@app.get("/")
async def index():
    res = await async_call()
    return res
    

async def async_call():
    lst = []
    async for value in async_call2(5):
        print(value)
        lst.append(value)
    return lst

async def async_call2(num):
    coros = [asyncio.create_task(asyncio.sleep(5)) for _ in range(5)]
    for task in asyncio.as_completed(coros):
        await task
        yield f"It's me!: "
        
        

    

if __name__ == "__main__":
    uvicorn.run(app, port=8000)