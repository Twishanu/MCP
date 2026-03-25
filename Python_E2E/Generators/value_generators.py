def making_chai():
    print("What chai would you like to have? ")
    order = yield
    count = 1
    while True:
        print(f"preparing chai: {count}-> {order}")
        order = yield # If I do not put this yield it will go on executing and won't wait for the next order
        count += 1

order = making_chai()
next(order) # starting the generator

order.send("Lemon Tea")
order.send("Masala Chai")
order.send("Milk Tea")