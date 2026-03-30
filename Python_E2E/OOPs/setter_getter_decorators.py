class Geeks:
    def __init__(self): ## constructor initializing nothing
        self._age = 0

    @property ## used for getter
    def age(self):
        print("getter function is called")
        return self._age
    
    @age.setter
    def age(self, x): ## setter function for validating then setting the value
        print("setter function is called")
        if x<=18:
            raise ValueError("Minimum age must be 18")
        else:
            self._age = x
        
geek = Geeks()
geek.age = 19  ## here age is used as a property not as a function because of @property
print(geek.age)


