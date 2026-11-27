
def hello(n):

    if n == 0:
        return
    
    print("Hello Python")

    hello(n - 1)

hello(5)



def test(n):

    if n == 0:
        return

    print(n)

    test(n - 1)

test(3)


# print 1 to 5 number
def number(n):

    if n == 6:
        return 

    print(n)

    number(n + 1)

number(1)



# print 5 to 1
def number(n):

    if n == 0:
        return

    print(n)

    number(n - 1)

number(5)



# Sum of Natural Numbers
def total(n):

    if n == 0:
        return 0 

    return n + total(n - 1)


print(total(5))



# ____________Factorial using recursion_______________
def factorial(n):

    if n == 0:
        return 1

    return n * factorial(n - 1)

print(factorial(5))


# Sum of Natural Numbers using Recursion
def total(n):

    if n == 0:
        return 0

    return n + total(n - 1)

print(total(5))


# Power of a Number using Recursion
def power(a, b):

    if b == 0:
        return 1

    return a * power(a, b - 1)

print(power(2, 3))


# Reverse a String using Recursion
def reverse(s):

    if s == "":
        return ""

    return reverse(s[1:]) + s[0]

print(reverse("NAZIR"))



# _______________Fibonacci______________
# fib(n) = fib(n-1) + fib(n-2) - THis is fibonacci formula

# def fibonacci(n):

#     if n <= 1:
#         return n

#     return fibonacci(n - 1) + fibonacci(n - 2)

# for i in range(7):
#     print(fibonacci(i), end=" ")


# fibonacci without recursion
# a = 0 
# b = 1

# for i in range(10):
#     print(a, end=" ")

#     c = a + b
#     a = b
#     b = c


# recursion with fibonacci
# def fib(n):
#     if n <= 1:
#         return n

#     return fib(n - 1) + fib(n - 2)

# print(fib(4))


# Practice
# def fib(n):
#     if n <= 1:
#         return n 

#     return fib(n - 1) + fib(n - 2)
# print(fib(0))

# print(fib(1))

# print(fib(2))

# print(fib(3))

# print(fib(4))