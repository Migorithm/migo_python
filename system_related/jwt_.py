from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

def generate_confirmation_token(self,expiration=300):
    s = Serializer("SECRET_KEY",expiration)
    return s.dumps({"confirm":self.id}).decode("utf-8") #PK of this instance

#----------------#----------------#----------------#----------------#----------------#----------------#----------------

class RegistrationForm():
    def validate_on_submit():
        pass
class User:
    pass
class SQLAlchemy:
    pass
class auth:
    @staticmethod
    def route(*args,**kwargs):
        def wrapper(func):
            def inner(*args,**kwargs):
                return func(**args,**kwargs)
            return inner
        return wrapper
    
db = SQLAlchemy()
user= User()

#----------------#----------------#----------------#----------------#----------------#----------------#----------------
from flask import Flask
from flask import render_template
class Message:
    pass
class mail:
    def send(self,msg):
        pass


app = Flask(__name__)

def send_email(to,subject,template,**kwargs):
    app = app
   
    msg = Message(app.config["MAIL_SUBJECT_PREFIX"]+ subject,
                  sender=app.config["MAIL_SENDER"],recipients=[to])
    msg.body = render_template(template+".txt", **kwargs)
    msg.html = render_template(template+".html", **kwargs)   #Here, we gonna look into /auth/email/confirm.txt and ~.html
   
    mail.send(msg)
    return 


#----------------#----------------#----------------#----------------#----------------#----------------#----------------


@auth.route('/register',methods=["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    password=form.password.data,
                    username=form.username.data)
        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmation_token()
        send_email(user.email,"Confirm Your account","auth/email/confirm",user=user,token=token)


@auth.route("confirm/<token>")
def confirm(token):
    if user.confirmed:
       pass
    if user.confirm(token):
        db.session.commit()
        
#----------------#----------------#----------------#----------------#----------------#----------------#----------------


def confirm(self,token):
    s = Serializer("SECRET_KEY") #use the same secret key
    try:
        data = s.loads(token.encode('utf-8'))   #load it
    except:
        return False
    if data.get('confirm') != self.id:
        return False
    self.confirmed = True  #confirmed. Not confirm.
    db.session.add(self)
    return True
