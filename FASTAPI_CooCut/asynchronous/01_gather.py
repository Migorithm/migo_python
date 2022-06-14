from fastapi import FastAPI
import asyncio
import uvicorn

app = FastAPI()

@app.get("/")
async def index():
    # asyncio.gather accepts one or more awaitable arguments and waits for all of them to complete, returning a list of results
    # for the given awaitables in the order they were submitted.
    lst : list = await asyncio.gather(*[async_call() for _ in range(5)]) #Possible to add coroutine directly. 
    return lst

async def async_call():
    await asyncio.sleep(5)
    return "Hey!"
    
if __name__ == "__main__":
    uvicorn.run(app, port=8000)