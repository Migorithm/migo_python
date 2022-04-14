class lst_cal:
    def __repr__(self):
        return  "[{}]".format(' '.join(map(str,self.lst)))
    def __init__(self):
        self.lst = []
        
    def push(self,element:int):
        assert isinstance(element,int), "Only int is allowed"
        self.lst.append(element)
    
    def __len__(self):
        return len(self.lst)  
      
    def __add__(self,other):
        assert len(self) == len(other), "list length must be the same"
        self.lst = [x+y for x,y in zip(self.lst,other.lst)]
        
        

a = lst_cal()
a.push(1)
a.push(56)
a.push(3)

b = lst_cal()
b.push(2)
b.push(50)
b.push(4)
print(a)

a+b

print(a)
