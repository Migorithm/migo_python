from flask import Flask,render_template,jsonify,request,session
import random ,os,json

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
random_number = random.random()

@app.route('/update_decimal',methods=["POST"])
def updatedecimal():
    random_number = random.random()
    posts= request.get_json()
    if posts["data"] =='1':
        random_number=1
    if posts["data"] =='2':
        random_number=2
    print(request.get_json())
    return jsonify("", render_template("random_decimal_model.html",x=random_number))
    #Instead of just returning html template, it renders things as json
    
@app.route('/')
def homepage():
    
    return render_template("home.html",x=random_number)

@app.route('/prac',methods=["GET","POST"])
def index():
    if request.method=="POST":
        print(request.get_json())
        print(request.get_data())
    return render_template("practice.html")

@app.route('/practice',methods=["POST"])
def whatever():
    info = json.loads(os.getenv("SOLUTION"))
    req= request.get_json()
    
    if req["P_NO"] in info.keys(): 
        print(info.keys())
        session["solution"] = req["P_NO"]
        return jsonify({"result": tuple(info[req["P_NO"]].keys()),"type":"cluster"})
    if req["P_NO"] in info[session["solution"]]:
        session["cluster"] = req["P_NO"]
        print(info[session["solution"]][session["cluster"]])
        return jsonify({"result":tuple(info[session["solution"]][session["cluster"]]),"type":"nodes"})
    return jsonify({"a":1,"b":3})




