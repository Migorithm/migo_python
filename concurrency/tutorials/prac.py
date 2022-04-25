import asyncio
async def get_burgers(number:int):
    burgers=[]
    for i in range(number):
        await asyncio.sleep(1)
        burgers.append("burgers")
    return burgers


burgers = get_burgers(2)