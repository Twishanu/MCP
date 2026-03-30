## using exception handling
file = open('Exception Handling/order_file.txt', 'w')
try: ## bcz file might crash in the memory ## safe way
    file.write("Hello orders")
except Exception as e:
    print(e)
finally:
    file.close()

## using with
with open('Exception Handling/order_file_2.txt', 'w') as file:
    ## two dunder methods of files are called __enter__ to write and __exit__ to close in background
    file.write("Hi orders")
