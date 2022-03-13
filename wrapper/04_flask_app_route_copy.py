import os

class FLASKY:
    def decoration_factory(self,path):
        def decorator(f):
            def wrapper(*args,**kwargs):
                print("Before function")
                print("http://{}:{}{}".format(os.getenv('http'),os.getenv('port'),path))
                result = f(*args,**kwargs)
                print("After function")
                return result
            return wrapper
        return decorator
        
app = FLASKY()

@app.decoration_factory("/")
def display(a,b,c,d):
    print(a+b+c+d)
    return a+b+c+d


print(display(1,2,3,4))