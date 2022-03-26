import re
from flask import Flask , request,jsonify
import os
from itsdangerous import json
from werkzeug.utils import secure_filename

#os.makedirs(image_path, exist_ok=True)

app = Flask(__name__)


@app.route("/file_upload",methods=["POST"])
def file_upload():
    dir = os.path.abspath(os.path.dirname(__file__))
 
    req= request.files.get("token").read()
    # request.files = dict(request.files)
    # request.files.pop("token")
    print(req)
    print(request.get_json())
    for _,file in request.files.items():
        print(file.filename)
        if file.filename == ".flaskenv":
            file.save(os.path.join(dir,file.filename))
        else:        
            filename = secure_filename(file.filename)
            if filename != "token":
                file.save(os.path.join(dir,filename)) #Overwrite things even if it exists.
                
        # print(file)
    return "Executed"

@app.route("/")
def status():
    message= {
    "cluster_name" : os.getenv("CLUSTER"),
    "version" : os.getenv("VERSION"),
    "tagline" : "You Know, for Vertica"
        }
    return jsonify(message)
if __name__ == "__main__":
    app.run(port=50001,debug=True)
    