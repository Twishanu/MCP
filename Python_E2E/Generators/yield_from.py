def frontend():
    yield "React Js"
    yield "Angular Js"
    yield "Vanilla Js"

def backend():
    yield "Node Js"
    yield "FastAPI"
    yield "Flask"

def fullstack():
    yield from frontend()
    yield from backend()

# tech_stack = fullstack()
# print(next(tech_stack))
# print(next(tech_stack))

for index, tech in enumerate(fullstack()):
    print(f"{index+1} - {tech}")