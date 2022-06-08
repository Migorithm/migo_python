import redis 
import datetime

r = redis.Redis(host="localhost",port=6379,db=0)

msg = f"[{datetime.datetime.now()}] hello, +____+ "
r.publish(channel="my_channel",message=msg)
print(f"Message is sent !!\n{msg}")