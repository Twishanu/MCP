import threading
import time

'''
Concurrency: Either through threading or asyncio
Multiprocessing: Parallelism
'''

def take_orders():
    for i in range(1, 4):
        print(f"Taking order for chai #{i}")
        time.sleep(2)

def brew_chai():
    for i in range(1, 4):
        print(f"Brewing chai #{i}")
        time.sleep(3)

## without threading
'''
take_orders()
brew_chai()
'''
### Wrapping each function into a thread object
order_thread = threading.Thread(target=take_orders)
brew_thread = threading.Thread(target=brew_chai)
## time.time() can also be used
start_time = time.perf_counter()
order_thread.start()
brew_thread.start()
### For exit... Without this, the program might exit early
order_thread.join()
brew_thread.join()
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Total time taken to execute: {elapsed_time}")
### Total time taken to execute: 9.00548950000666
### Total time taken to execute: 9.005212099989876
'''
Time →   0    2    3    4    6    9

Orders → [1]--[2]--[3]--------END
Brew   → [1]-----[2]-----[3]------END
'''