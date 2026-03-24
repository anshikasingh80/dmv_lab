try:
    print(x)
except NameError:
    print("x was not defined. Setting default value.")
    x = 10

print("x =", x)


data = {"name": "Shradha"}

age = data.get("age", 25) 
print("age =", age)

def greet(name=None):
    if name is None:
        name = "Guest"
    print("Hello,", name)

greet()

