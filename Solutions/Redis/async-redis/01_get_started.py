import asyncio
import aioredis

async def main():
    #Redis client bount to single connection (no auto reconnection).
   
    redis = await aioredis.Redis(
        host="localhost",port=6379,db=0
    )
    await redis.set('my-key','value')
    val = await redis.get('my-key')
    print(val)
    
    await redis.close()
    
    



if __name__ == '__main__':
    asyncio.run(main())
