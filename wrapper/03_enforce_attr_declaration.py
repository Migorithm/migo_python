from functools import wraps


class  MissingAttributeError(Exception):
    pass

def requires(*required_attrs):
    def wrapper(method):
        @wraps(method)
        def inner_wrapper(self,*args,**kwargs):
            if not all(hasattr(self,attr) for attr in required_attrs):
                raise MissingAttributeError()
            return method(self,*args,**kwargs)
        return inner_wrapper
    return wrapper

class Test(object):    
    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            setattr(self,k,v)
        self.something()

    @requires('HAM')
    def something(self):
        return 'Done'

t = Test(HAM="spam",FRUIT="strawberry")

t.something()
