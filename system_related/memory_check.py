import memory_profiler as mem_pro
from functools import wraps
def decorator_function(orig_func):
    @wraps(orig_func)
    def wrapper(*args,**kwargs):
        print("memory usage before the function : {}MB".format(mem_pro.memory_usage()))
        result=orig_func(*args,**kwargs)
        print("memory usage after the function : {}MB".format(mem_pro.memory_usage()))
        return result
    return wrapper

@decorator_function
def looper(num):
    rst=[]
    for i in range(num):
        if i%2 ==0:
            rst.append(i)
    return rst

looper(10000000)
