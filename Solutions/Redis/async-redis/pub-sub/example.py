import asyncio
import aioredis


def reader(json:dict):
    print(f"processing json data... {json}")
    return True

async def main():
    sub = await aioredis.Redis(
        host="localhost",
        port=6379,
        db=0,
        decode_responses=True,
        )

    s = sub.pubsub()    
    await s.subscribe('chan:1')
    while True:
        print("waiting message...")
        res = await s.get_message(timeout=5)
        if res and res.get("type") == "message" :
            print(res.get("data"))
            tsk = await asyncio.to_thread(reader,res)
            if tsk:
                print(f"Process on {tsk} succeeded!")
    
if __name__ == '__main__':
    asyncio.run(main())
    aioredis.pub