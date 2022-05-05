from functools import lru_cache, wraps
from datetime import datetime, timedelta


def timed_lru_cache(seconds: int, maxsize: int = 128):
    def wrapper_cache(func):
        func = lru_cache(maxsize=maxsize)(func)
        func.lifetime = timedelta(seconds=seconds)  
        func.expiration = datetime.utcnow() + func.lifetime
        @wraps(func)
        def wrapped_func(*args, **kwargs):
            if datetime.utcnow() >= func.expiration:
                func.cache_clear()
                func.expiration = datetime.utcnow() + func.lifetime
            print(func.cache_info())
            return func(*args, **kwargs)
        return wrapped_func
    return wrapper_cache


@timed_lru_cache(5)
def calculator(x,y):
    
    return x*y



