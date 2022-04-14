
class Employee():
    raise_amount= 1.04
    num_of_emps = 0
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email = first + "." + last + "@company.com"
        
        #Every time instance is added, it will be increased
        Employee.num_of_emps +=1 

#The following will show all the attributes and methods that belong to the class
print(Employee.__dict__)

#The instance __dict__ on the other hand, will show you only things that are specific to this instance
e1 =Employee("Jonh","Doh",10000)
print(e1.__dict__)

e2 =Employee("Jonh","Doh",10000)
print(e2.__dict__)

print(Employee.num_of_emps)

