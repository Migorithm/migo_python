from flask import Flask,render_template,jsonify,request
import random

app = Flask(__name__)

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

@app.route('/prac')
def index():
    return render_template("practice.html")

@app.route('/practice',methods=["POST"])
def whatever():

    req= request.get_json()
    if req["P_NO"] == "Redis":
        return jsonify({"result":[1,2,3,4,5]})
    if req["P_NO"] == "Elastic":
        return jsonify({"result":[1,2,3,4,5]})
    return jsonify({"a":1,"b":3})

app.run(debug=True)

