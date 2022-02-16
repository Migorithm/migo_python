from functools import wraps
#logging
def my_logger(orig_func):
    import logging
    #Setting up the logfile that matches the name of original function
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__),level=logging.INFO)
    
    wraps(orig_func)
    def wrapper(*args,**kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args,kwargs)
        )
        return orig_func(*args,**kwargs)
    return wrapper

# Log form will be ::
    # INFO:root:Ran with args: ('John', 25), and kwargs: {} 

# Use case
@my_logger
def display_info(name,age):
    print("disply_info ran with arguments ({},{})".format(name,age))

display_info("John",25)