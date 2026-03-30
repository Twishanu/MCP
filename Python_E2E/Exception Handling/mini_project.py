# class InvalidChaiError(Exception): pass

# def generate_bill(flavor, cups):
#     menu = {
#         "masala" : 20,
#         "ginger" : 15,
#         "lemon" : 20,
#     }
#     try:
#         if flavor not in menu:
#             raise InvalidChaiError("Sorry we do not serve that flavor :<")
#         if not isinstance(cups, int):
#             raise TypeError("No. of cups must be an integer")
#         bill = menu[flavor] * cups
#         print(f"Your total bill is: {bill}")

#     except InvalidChaiError as e:
#         print(f"Error: {e}")
#     except TypeError as e:
#         print(f"Error: {e}")
#     except Exception as e:
#         print(f"Error: {e}")

#     else:
#         print("chai is ready...")
#     finally:
#         print("Please visit us again")

# generate_bill("masala", 2)

class InvalidChaiError(Exception):
    pass

def generate_bill(flavor, cups):
    menu = {
        "masala": 20,
        "ginger": 15,
        "lemon": 20,
    }

    if flavor not in menu:
        raise InvalidChaiError("Sorry we do not serve that flavor :<")

    if not isinstance(cups, int):
        raise TypeError("No. of cups must be an integer")

    return menu[flavor] * cups


### chatgpt recommended to raise errors in the called function but handle errors in the main function
try:
    bill = generate_bill("masala", 2)
    print(f"Your total bill is: {bill}")
    print("chai is ready...")
except InvalidChaiError as e:
    print(f"Error: {e}")
except TypeError as e:
    print(f"Error: {e}")
finally:
    print("Please visit us again")

    