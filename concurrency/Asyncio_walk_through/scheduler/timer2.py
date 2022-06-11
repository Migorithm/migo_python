import asyncio
from db import User
from sqlalchemy.orm import Session
from db import async_session

class Timer:
    def __init__(self, interval, first_immediately, timer_name, context, callback):
        self._interval = interval
        self._first_immediately = first_immediately
        self._name = timer_name
        self._context = context
        self._callback = callback
        self._is_first_call = True
        self._ok = True
        self._task = asyncio.ensure_future(self._job())
        print(timer_name + " init done")

    async def _job(self):
        try:
            while self._ok:
                if not self._is_first_call or not self._first_immediately:
                    await asyncio.sleep(self._interval)
                await self._callback(self._name, self._context, self)
                self._is_first_call = False
        except Exception as ex:
            print(ex)

    def cancel(self):
        self._ok = False
        self._task.cancel()


async def some_callback(timer_name, context, timer):
    context['count'] += 1
    print('callback: ' + timer_name + ", count: " + str(context['count']))
    if timer_name == 'Timer 2' and context['count'] == 3:
        timer.cancel()
        print(timer_name + ": goodbye and thanks for all the fish")

async def insert(timer_name,context,timer):
    context['count'] += 1
    print('callback: ' + timer_name + ", count: " + str(context['count']))
    async with async_session() as session:
        async with session.begin():
            user = User(name=timer_name+context["count"])
            await session.add(user)
            await session.commit()


async def get(timer_name,context,timer):
    context['count'] += 1
    print('callback: ' + timer_name + ", count: " + str(context['count']))
    async with async_session() as session:
        async with session.begin():
            users = session.query(User).all()
            print(users)



def main():
    timer1 = Timer(interval=1, first_immediately=True, timer_name="Timer 1", context={'count': 0}, callback=insert)
    timer2 = Timer(interval=5, first_immediately=False, timer_name="Timer 2", context={'count': 0}, callback=get)
    try:
        loop = asyncio.get_running_loop()
        loop.run_forever()
    except KeyboardInterrupt:
        timer1.cancel()
        timer2.cancel()
        print("clean up done")

if __name__ =="__main__":
    main()