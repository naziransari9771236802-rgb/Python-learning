# Function ko Argument me pass karna
def greet():
    print("Hello Nazir")

def welcome(func):
    func()

welcome(greet)


# Function ko return krna
def outer():

    def inner():
        print("Hello Nazir")

    return inner

result = outer()

result()



# real example
def add(a, b):
    return a + b

def calculate(func, a, b):
    return func(a, b)

result = calculate(add, 10, 20)

print(result)



def square(n):
    return n * n

def calculate(func, n):
    return func(n)

result = calculate(square, 6)
print(result)


# dusre function ko argument mein accept krna
def cube(n):
    return n * n * n

def calculate(func, n):
    return func(n)

result = calculate(cube, 5)

print(result)



def add(a, b):
    return a + b

def adding(func, a, b):
    return func(a, b)

result = adding(add, 20, 30)
print(result)




# _________Function Returning Another Function__________.
def outer():

    def inner():
        print("Hello Bhai")

    return inner

result = outer()

result()



# Practice________
def outer():

    def inner():
        print("Python Developer")

    return inner

result = outer()

result()



def multiplier():

    def multiply(a, b):
        return a * b
    return multiply
result = multiplier()

answer = result(5, 10)

print(answer)