def make_special_chai(*args, **kwargs): ## args-->tuple, kwargs-->'dict' so they always expect keyword based arguments
    """This method is used to take ingredients as arguments for making chai"""
    print(f"Ingredients: {args}")
    print(f"Toppings: {kwargs}")


### calling
make_special_chai("Lemon tea", "ginger", "chai masala", milk="no", foam="no")
print(make_special_chai.__doc__)
print(make_special_chai.__name__)