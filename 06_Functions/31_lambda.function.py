# Normal function
def square(x):
    return x * x

print(square(5))

# Syntax______
# lambda = Keyword
# arguments = Parameters
# expression = Operation

# lambda arguments: expression  # this is syntax

# Lambda Function
square = lambda x: x * x
print(square(5))


# Addition_______
add = lambda a, b: a + b

print(add(10, 20))


# Even or Odd_____
check = lambda x: "Even" if x % 2 == 0 else "Odd"

print(check(7))


# Practice______
# square nikalna
square = lambda x: x * x

print(square(8))


# Addition 
add = lambda a, b, c: a + b + c

print(add(10, 20, 30))



# Even or Odd
checking = lambda number: "Even" if number % 2 == 0 else "Odd"

print(checking(17))


# Find Maximum number
max_number = lambda a, b: a if a > b else b

print(max_number(45, 78))


# Average nikalna___
average = lambda a, b, c: (a + b + c) / 3

print(average(10, 20, 30))