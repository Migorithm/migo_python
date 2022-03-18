from flask import Flask , request,jsonify
from itsdangerous import json
import requests

app = Flask(__name__)


res=requests.post("http://127.0.0.1:50001/test",json={"token":1})
print(res.json())
    

    