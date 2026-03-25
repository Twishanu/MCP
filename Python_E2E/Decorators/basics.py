from functools import wraps

### Used to decorate functions
def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before the function")
        func()
        print("After the function")
    return wrapper

@my_decorator
def greet():
    print("Hi from the greet function...")

greet()

print(greet.__name__) ## name changes to wrapper so we have to use 'wraps'