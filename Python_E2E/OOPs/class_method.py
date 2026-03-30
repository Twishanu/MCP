class MakingChai:
    def __init__(self, tea_type, toppings, size):
        self.tea_type = tea_type
        self.toppings = toppings
        self.size = size

    @classmethod ## It is used to handle arguments in other forms which are not defined in __init__
    ## It then makes it __init__ friendly
    def fromString(cls, full_order_data):
        tea_type, toppings, size = full_order_data.split("-")
        return cls(
            tea_type, toppings, size
        )
    
    @classmethod
    def fromDict(cls, full_order_data):
        tea_type = full_order_data["tea_type"]
        toppings = full_order_data["toppings"]
        size = full_order_data["size"]

        return cls( ###### this parses it into __init__ language cls--class which in turn means __init__
            tea_type, toppings, size
        )

    def displayChai(self):
        return f"Your desired tea type is: {self.tea_type} with toppings: {self.toppings} and size: {self.size}"
    
chai_1 = MakingChai("Masala", "no", "large")
chai_2 = MakingChai.fromString("Lemon-ice-medium") ## In a string format

chai_3 = MakingChai.fromDict({
    "tea_type": "Green",
    "toppings": "pepper",
    "size": "small"
})

print(chai_1.displayChai())
print(chai_2.displayChai())
print(chai_3.displayChai())
