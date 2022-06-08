import redis

r = redis.Redis(host="localhost",port=6379,db=0)
s = r.pubsub() 

s.subscribe("my_channel")

while True:
    print("waiting message...")
    res = s.get_message(timeout=5)
    if res and res.get("type") == "message" :
        print(res.get("data").decode("utf-8"))
        