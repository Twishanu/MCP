'''
Threading:

One worker switching tasks quickly
(“take order → check chai → take order…”)
Multiprocessing:

Two workers:
One only takes orders 👨‍🍳
One only brews chai 🔥

👉 Work actually happens at the same time
'''
import multiprocessing
import time

def take_orders():
    for i in range(1, 4):
        print(f"Taking order for chai #{i}")
        time.sleep(2)

def brew_chai():
    for i in range(1, 4):
        print(f"Brewing chai #{i}")
        time.sleep(3)



if __name__ == "__main__":
    take_orders_worker = multiprocessing.Process(target=take_orders)
    brew_worker = multiprocessing.Process(target=brew_chai)
    ## time.time() can also be used
    start_time = time.perf_counter()

    take_orders_worker.start()
    brew_worker.start()

    take_orders_worker.join()
    brew_worker.join()

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Total time taken to execute: {elapsed_time}")
    ### Total time taken to execute: 9.19213639991358
    ### Total time taken to execute: 9.203547799959779

    ### For a huge timeline-- multiprocessing is better, also it can tackle GIL bottleneck