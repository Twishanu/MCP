def get_chai_gen():
    yield "cup 1"
    yield "cup 2"
    yield "cup 3"

chai = get_chai_gen()
print(next(chai))
print(next(chai))
print(next(chai))
