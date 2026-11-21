# Simple function
def greet():
    print("Hello, Welcome to Python!")
greet()


# Function with parameters
def greet(name):
    print("Hello", name)
greet("Nazir")


# function with Return
def add(a, b):
    return a + b

result = add(10, 20)
print(result)



def add(a, b):
    return a + b
result = add( 10, 30)
print(result)


# square nikalna
def square(a):
    return a * a
result = square(5)
print(result)


# Even/Odd nikalna
def check_even_odd(num):
    if num % 2 == 0:
        return "Even Number"
    else:
        return "Odd Number"

result = check_even_odd(7)
print(result)



# create three numbers and return the largest number
def largest_number(a, b, c):

    if a >= b and a >= c:
        return a

    elif b >= a and b >= c:
        return b

    else:
        return c

result = largest_number(10, 25, 15)
print(result)



# input() inside Function
def get_name():
    name = input("Enter your name: ")
    print("Welcome", name)

get_name()



# len() inside Function
def count_character():
    name = input("Enter your name: ")
    print("Total character:", len(name))

count_character()



# type() inside Function
def check_type():
    value = 100
    print(type(value))

check_type()


# range() inside Function
def print_numbers():
    for i in range(1, 11):
        print(i)

print_numbers()



# sum() inside Function
def calculate_sum():
    numbers = (10, 29, 43)
    print(sum(numbers))

calculate_sum()



# max() inside Function
def find_largest():
    number = [10, 20, 30]
    print(max(number))

find_largest()



# min() inside Function
def find_smallest():
    numbers = [10, 30, 20, 60]
    print(min(numbers))

find_smallest()



# sorted() inside Function
def sort_numbers():
    numbers = [50, 30, 40, 60, 10]
    print(sorted(numbers))

sort_numbers()



