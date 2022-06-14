from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from db import get_db,User
# from fastapi_utils.tasks import repeat_every
from repeat_scheduler_with_arguments import repeat_every
from random import choice
from string import ascii_letters
from pydantic import BaseModel


app = FastAPI()
class UserOut(BaseModel):
    id: int
    name: str
    class Config:
        orm_mode = True


def insert(db:Session,message) -> None:
    user = User(name=message)
    db.add(user)
    db.commit()
    print(message)
    
@app.on_event("startup")
@repeat_every(seconds=5)
def index() -> None:
    try:
        db = next(get_db())
        insert(db,"from index")
    except Exception as e:
        print("why error?")
        print(e)
    finally:
        pass
    
    print("dsd")
    return "Nothing"


@app.get("/haha") #This will trigerred only after it is hit 
@repeat_every(seconds=5)
def whatever(db:Session = Depends(get_db)):
    insert(db,"from whatever")
    

@app.get('/users',response_model=list[UserOut])
def users(db:Session = Depends(get_db))->None:
    users= db.query(User).all()
    return users