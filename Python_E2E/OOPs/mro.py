class A:
    label = "Tea"

class B(A):
    label = "Masala Tea"
class C(A):
    label = "Lemon Tea"

class D(B, C):
    pass ## which label to be used???


cup = D()
print(cup.label) ## depends on the order of inheritence (Method Resolution Order)
print(D.__mro__) ## (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)