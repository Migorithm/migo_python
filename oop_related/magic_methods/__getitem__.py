## Magic method for square brackets. It lets you reference foo[0], foo[1], etc 

class UniqueList:
    def __init__(self, items):
        self.items = []
        for item in items:
            self.append(item)
    def append(self, item):
        if item not in self.items:
            self.items.append(item)
    def __getitem__(self, index):
        return self.items[index]
    
a= UniqueList([1,2,3,4])
print(a[0]) # 0

a.append(3) #not working
print(a.items) 