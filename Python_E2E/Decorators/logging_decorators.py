from functools import wraps
def my_decorator(func):
    '''ideal decorator with logger'''
    ## TypeError: making_chai() takes 0 positional arguments but 2 were given if i dont pass arg here too

    ## I can also hardcode flavor, milk but in that case I have to change the decorator everytime I change the function args
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"🚗 Executing function {func.__name__}")
        result = func(*args, **kwargs)
        print(f"✅ Finished executing function {func.__name__}")
        return result  ## for the func
    return wrapper ## after adding the wrapper return

@my_decorator
def making_chai(flavor, milk="no"):
    print(f"Brewing chai : {flavor} and milk status : {milk}")

making_chai("Milk Tea", milk = "yes")
making_chai("Green Tea")