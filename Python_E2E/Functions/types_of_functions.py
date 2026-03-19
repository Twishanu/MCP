## pure vs impure functions
def pure_chai(cups):
    return cups * 10

total_cups = 10
print(pure_chai(total_cups))
print("Total cups: ", total_cups)
## impure not recommended
def impure_chai(cups):
    global total_cups
    total_cups = total_cups * 10

impure_chai(total_cups)
print("Total cups: ", total_cups)
    
## recursive functions
def pour_chai(cups):
    if cups==0:
        return "All cups poured"
    print("pouring...")
    return pour_chai(cups-1)
res = pour_chai(3)
print(res)

## lambda functions
## a(func name) = lambda x(arg):x*2(exp)
check = lambda x: "positive" if x>0 else "negative" if x<0 else "zero"
print(check(3))



## without lambda

# strong_chai_types = []
# def making_strong_chai(chai_types):
#     for chai in chai_types:
#         if chai == "kadak":
#             strong_chai_types.append(chai)
# # filter(function, iteratable)

# def making_strong_chai(chai):
#     if chai == "kadak":
#         return chai
# # filter(function, iteratable)
chai_types = ["light", "kadak", "ginger", "kadak"]
# making_strong_chai(chai_types)
# print(strong_chai_types)

# res = lambda chai : chai + "123"
# print(res("hello"))

# strong_chai_types = list(filter(making_strong_chai, chai_types))
strong_chai_types = list(filter(lambda chai : chai=="kadak", chai_types))
print(strong_chai_types)


        