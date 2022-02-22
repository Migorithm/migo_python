from functools import wraps

def timer(func):
    import time
    @wraps(func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args,**kwargs)
        t2 = time.time() -t1 
        print(f"{func.__name__} ran in : {t2} sec")
    return wrapper    


def decorator_function(func):
    @wraps(func)
    def wrapper_function(*args,**kwargs):
        print('Before function....')
        result =func(*args,**kwargs)
        print("After function...")
    return wrapper_function


@timer
@decorator_function
def display(name,age,height,school=None):
    """ This will display things about you!"""
    print(f"Hi {name}! You are fucking {age} years old! and {height}cm! from {school}")


### Factory
def http_prefix(prefix):
    def decorator_function(func):
        @wraps(func)
        def wrapper_funcion(*args,**kwargs):
            http_prefix = f"http://localhost:9200/{prefix}";
            print(f"Prefix of this endpoint is {http_prefix}");
            result = func(*args,**kwargs);
            return result
        return wrapper_funcion
    return decorator_function


@http_prefix("myhome")
def show(curl):
    print("rerere {}".format(curl))
