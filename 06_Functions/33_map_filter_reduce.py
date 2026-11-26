# ____________map()_____________
# map() kisi function ko list ke har element par apply karta hai.
# number ka square
number = [1, 2, 3, 4, 5]

def square(n):
    return n * n

result = map(square, number)

print(list(result))



# numbers ka multiply
numbers = [10, 20, 30, 40, 50]

def multiply(n):
    return n * 2

result = map(multiply, numbers)

print(list(result))



# ___________map() + lambda_____________
numbers = [2, 4, 6, 8, 10]

result = map(lambda n: n * n, numbers)

print(list(result))



numbers = [5, 10, 15, 20, 25]

result = map(lambda n: n * 3, numbers)

print(list(result))



numbers = [10, 15, 20, 25, 30]

result = map(lambda n: n + 5, numbers)

print(list(result))



# Real-World Example 1: Shopping Cart
prices = [500, 1000, 1500, 2000]

final_prices = map(lambda price: price + (price * 18 / 100), prices)

print(list(final_prices))


# Employee Salary
salaries = [20000, 25000, 30000, 35000]

updated_salary = map(lambda salary: salary + 5000, salaries)

print(list(updated_salary))




# __________________________filter() + lambda_________________

# filter() kisi list mein se condition ke according elements ko select karta hai.

# Real-World Example: Employee Selection

salaries = [15000, 25000, 35000, 40000, 50000]

result = filter(lambda salary: salary > 30000, salaries)

print(list(result))



# shopping prices
prices = [199, 499, 999, 1499, 2499, 2999]

result = filter(lambda price: price > 1000, prices)

print(list(result))



# Student Result
marks = [25, 35, 45, 55, 65, 75, 85, 95]

result = filter(lambda mark: mark >= 40, marks)

print(list(result))



# Age verification 
ages = [12, 16, 18, 21, 25, 15, 30, 17]

result = filter(lambda age: age >= 18, ages)

print(list(result))



# E- commerce order management_____
orders = [450, 1200, 250, 3000, 750, 5000, 150]

result = filter(lambda amount: amount >= 500 and amount <= 3000, orders)

print(list(result))



# employee Data Filtering
employees = [
    {"name": "Rahul", "age": 22, "salary": 25000},
    {"name": "Aman", "age": 28, "salary": 45000},
    {"name": "Neha", "age": 24, "salary": 35000},
    {"name": "Priya", "age": 30, "salary": 60000},
    {"name": "Arjun", "age": 21, "salary": 20000}
]

result = filter(lambda employee: employee["age"] >= 25 and employee["salary"] > 30000, employees)

print(list(result))




# ________________reduce()_________________
# reduce() list ke saare elements ko combine karke ek single result deta hai.

# shopping cart, calculate product bill

from functools import reduce
prices = [500, 1000, 1500, 2000, 2500]

total = reduce(lambda a, b: a + b, prices)

print("Total Price:", total)




# Higher prices
from functools import reduce

prices = [450, 1200, 800, 2500, 1500, 3000]

total = reduce(lambda a, b: a if a > b else b, prices)

print("Total Price:", total)



# Employee Salary Calculation
from functools import reduce
salaries = [20000, 25000, 30000, 35000, 40000]

salary = reduce(lambda a, b: a + b, salaries)

print("Total Price:", salary)



# Bank Account Balance
from functools import reduce

transactions = [5000, -2000, 3000, -1000, 4000]

balance = reduce(lambda a, b: a + b, transactions, 0)

print("Final Balance:", balance)