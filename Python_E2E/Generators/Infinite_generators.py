def infinite_chai():
    count = 1
    while True:
        yield f"Refil #{count}"
        count += 1

refil = infinite_chai() ## With loop I can get as many refils as I want
for _ in range(12):
    print(next(refil))
