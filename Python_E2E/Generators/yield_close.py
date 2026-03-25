def chai_stall():
    try:
        order = yield
        while True:
            print(f"preparing order {order}")
            order = yield
    except:
        print("No new orders")

stall = chai_stall()
next(stall) # starting the generator
stall.send("Lemon Tea")
stall.send("Green Tea")

stall.close() ## best practice