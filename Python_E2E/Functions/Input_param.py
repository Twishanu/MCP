### parameters --- method arguments
##arguments--while calling the method

def make_chai(tea, milk, sugar):
    print(f"tea: {tea}, milk: {milk}, sugar: {sugar}")
    
make_chai("Darjeeling", "yes", "yes") ## since I already know the positions so keywords are nmot imp (Positional arguments)
make_chai(tea="Green", sugar="no", milk="no") ## keyword based..positions not required

#args and kwargs
def make_special_chai(*args, **kwargs): ## args-->tuple, kwargs-->'dict' so they always expect keyword based arguments
    print(f"Ingredients: {args}")
    print(f"Toppings: {kwargs}")


### calling
make_special_chai("Lemon tea", "ginger", "chai masala", milk="no", foam="no")

## list is mutable
def change_list(list):
    list[1] = 50

a = [1, 2, 3]
change_list(a)
print(a)

## string cant be changed like this ---- diff location in the memory
def change_string(str):
    str = str + "twishanu"
b = "hello"
change_string(b)
print(b)

c = "hello"
c = c + " world"
print(c)
    