import redis

def main():
    r = redis.Redis(host="localhost",port=6379,db=0,decode_responses=True)
    s = r.pubsub()
    s.subscribe("chat")
    s.subscribe("event")
    
    while True:
        print("waiting message...")
        res = s.get_message(ignore_subscribe_messages=True,timeout=5)
        if res:
            print(res)
            handle_message(res["channel"],res["data"])

def handle_message(topic:str, message:str):
    if topic == "chat":
        handle_message_for_chat(message)
    else:
        print(f"handler for {topic} doesn't exist!")

def handle_message_for_chat(message:str):
    print(message)
    
if __name__ == "__main__":
    main()