from functools import wraps

def auth_gate(func):
    @wraps(func) 
    def wrapper(*args, **kwargs):
        ## getting the user role from kwargs or args
        user_role = kwargs.get('role') if "role" in kwargs else args[0]
        if user_role != "admin":
            print(f"Access denied for user- {user_role}: Admins only")
            return None
        else:
            return func(*args, **kwargs)
    return wrapper
    
@auth_gate
def auth_access(role, name):
    print(f"Access granted to {name} with role: {role}")

auth_access("user", name="Twishanu")
auth_access(role = "admin", name="root")
