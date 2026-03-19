### calling a func with no defined return statement----> None
def test_report():
    return 100, 60, 30 # 100 executed, 60 left

a, b, _ = test_report() ## it returns a tuple --> so we can unpack the tuple into two variables
# incase of three return values we can use _
print(f"Tests executed: {a}, Tests left: {b}") 

def test_func(**kwargs):
    print(kwargs)
    
# test_func(total_tests=100) ## wrong keyword arguments don't work
test_func(total_tests=100) ## wrong keyword arguments don't work --- so better to use **kwargs