
class BendingMachine:
    @staticmethod
    def MixCoffee():
        return Mixer()\
            .add_sugar()\
            .add_cream()\
            .add_bean()\
            .get_result()
    @staticmethod
    def BlackAmericano():
        return Mixer()\
            .add_bean()\
            .add_bean()\
            .add_bean()\
            .get_result()

class Mixer(): #builder
    def __init__(self):
        self.product = Product()
    
    def add_sugar(self):
        self.product.fomular.append("sugar")
        return self
    def add_cream(self):
        self.product.fomular.append("cream")
        return self
    def add_bean(self):
        self.product.fomular.append("bean")
        return self
    def get_result(self):
        dic ={}
        for ingredient in self.product.fomular :
            if ingredient not in dic:
                dic[ingredient] =1 
            else :
                dic[ingredient] +=1
        return dic
    
class Product:
    def __init__(self):
        self.fomular = []
        
    

coffee = BendingMachine.MixCoffee()
print(coffee)

blackcoffee = BendingMachine.BlackAmericano()
print(blackcoffee)