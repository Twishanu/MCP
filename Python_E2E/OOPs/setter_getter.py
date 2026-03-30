class Greet:
    def __init__(self, age=0):
        self._age = age ## __var is conventionally treated as a private variable

    def get_age(self):
        return self._age
    
    def set_age(self, age): ## setter is used in Python for validation
        if age >= 18:
            self._age = age
        else:
            raise ValueError("Age must be not less than 18")

greet = Greet()
greet.set_age(18)
print(greet.get_age())