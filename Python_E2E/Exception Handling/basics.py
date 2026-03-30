def making_chai_simple(chai):
    menu = {
        1: "masala chai",
        2: "green tea",
        3: "Lemon tea",
        4: "Iced tea"
    }

    for options in menu.values():
        if chai==options:
            print(f"Serving you {chai}")
            return 
    raise ValueError("We do not have your desired order")
    
### Using try except else finally
def making_chai(chai):
    menu = {
        1: "masala chai",
        2: "green tea",
        3: "Lemon tea",
        4: "Iced tea"
    }
    try:
        for options in menu.values():
            if chai==options:
                print(f"Serving you {chai}")
                break
        else: ### for-else syntact --- executes if no break/return
            raise Exception("We do not serve your desired order")
    except Exception as e:
        ## handling
        print(f"Error: {e}")
    else: #### else will only execute when no exception
        print("Thank you visit again")
    finally: ## Python says: "Before leaving the try block (even via return), I must execute finally."
        print("Next customer please")


            


making_chai("masala chai")
making_chai("ginger tea")