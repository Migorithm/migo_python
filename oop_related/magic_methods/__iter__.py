"""
Iterator protocol: Object that supports the __iter__ and __next__
"""

#Iterating forever

class Repeater:
    def __init__(self,value):
        self.value = value
    
    def __iter__(self):
        return RepeaterIterator(self)

class RepeaterIterator:
    def __init__(self,source):
        self.source = source
    
    def __next__(self):
        return self.source.value
    
repeater = Repeater("Hello")

# for item in repeater:
#     print(item) #Ininite loop


iterator = repeater.__iter__() #It first prepared the repeater object for iteration by calling its __iter__ method

print(iterator.__next__()) #The loop repeatedly called the iterator object's __next__ method to retrive values from it.



"""
Simpler Iterator class
"""
class Repeater:
    def __init__(self,value):
        self.value = value
    
    def __iter__(self):
        return self
    def __next__(self):
        return self.value


"""
However... who wants to iterate forever?

Clearly, infinite repetition isn't the main use case for iterators in Python. 
"""
my_list = [1,2,3]
iterator = iter(my_list)
print(next(iterator)) #1
print(next(iterator)) #2
print(next(iterator)) #3
try:
    print(next(iterator)) #Stop Iteration
except StopIteration:
    print("Stop Iteration!")


class BoundedRepeater:
    def __init__(self,value,max_repeats):
        self.value = value
        self.max_repeats = max_repeats
        self.count =0 
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count >= self.max_repeats:
            raise StopIteration
        self.count+=1
        return self.value
    
repeater = BoundedRepeater("Hello?",5)
for item in repeater:
    print(item)
    
"""
Every time next() is called in the loop, we check for a StopIteration exception and break the while loop if necessary.
"""


"""
Generators are simplified iterators.
When a yield is invoked, it also passes control back to the caller of the function - but it only does so temporarily.

Whereas a return statement disposes of a function's local state, a yield statement suspends the function and retains
its local state.
"""

def repeater(value):
    while True:
        yield value 
        
rep = repeater(5)
print(next(rep))
print(next(rep))
print(next(rep))
print(next(rep))



def bounded_repeater(value, max_repeats):
    count = 0
    while True:
        if count>= max_repeats:
            return
        count +=1
        yield value
        
for x in bounded_repeater("hi",4):
    print(x)
    
def simpler_bounded_repeater(value,max_repeats):
    for _ in range(max_repeats):
        yield value

