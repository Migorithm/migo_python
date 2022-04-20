import json

load_json=json.load(open("./telekey.json"))
urls = tuple("https://api.telegram.org/bot{}/sendMessage?parse-mod=html&chat_id={}".format(dic.get("KEY"),dic.get("CHAT_ID")) for dic in load_json)
print(urls)