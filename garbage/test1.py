from flask import Flask , request,jsonify
from itsdangerous import json

app = Flask(__name__)


@app.route("/test",methods=["POST"])
def test():
    req= request.get_json()
    if req.get("token"):
        return jsonify(dict(config()))

def config():
    with open("../file_handling/redis_file/redis.conf") as handle:
        print("d")
        for line in handle:
            if  line != '\n' and not line.startswith("#"):
                key,value= line.lstrip().split(" ",1)
                value = value.replace("\n","")
                yield key, value

if __name__ == "__main__":
    app.run(port=50001)
    
    