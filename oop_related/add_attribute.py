#### How to add more attribute to the instance of the different object? 



class Person:
    def __init__(self,age,name):
        self.AGE : int = age
        self.NAME : str = name

p1 = Person(10,"Jun")
p2 = Person(5,"John")

class Crying: 
    @staticmethod
    def crying(person:Person):
        if getattr(person,"AGE") > 8:
            person.crying = "baby crying"
        else:
            person.crying = "adult crying"


Crying.crying(p1)

print(p1.crying)