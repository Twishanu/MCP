## creating custom errors
class OutOfIngredientsError(Exception):
    pass

def making_chai(*args, **kwargs):
    milk = kwargs.get("milk") if "milk" in kwargs else args[0]
    sugar = kwargs.get("sugar") if "sugar" in kwargs else args[0]

    if milk == 0 or sugar == 0:
        raise OutOfIngredientsError("Sorry we are unable to serve you now :<")
    else:
        print("Making chai...")

making_chai(1, milk=1)
