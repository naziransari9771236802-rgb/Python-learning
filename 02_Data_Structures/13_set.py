# set___
numbers = {10, 20, 30, 40, 50}
print(numbers)


# Duplicate values are not allowed
numbers = {10, 20, 30, 40, 10, 10, 20}
print(numbers)


# Empty set
my_set = set()
print(type(my_set))


# Set does not follow a fixed order
my_set = {"Apple", "Banana", "Mango"}
print(my_set)


# Set can store different data types
my_set = {10, "Hello", 20.5, True}
print(my_set)


# Length of set
numbers = {10, 20, 30, 40, 50}
print(len(numbers))


# Check item exists or not
numbers = {10, 20, 30, 40, 50}
print(20 in numbers)
print(100 in numbers)


# Set Union ( | )
set1 = {10, 20, 30}
set2 = {30, 40, 50}
print(set1 | set2)


# Set Intersection ( & )
set1 = {10, 20, 30}
set2 = {20, 30, 40}
print(set1 & set2)


# Set Difference ( - )
set1 = {10, 20, 30}
set2 = {20, 30, 40}
print(set1 - set2)


# Set Symmetric Difference ( ^ )
set1 = {10, 20, 30}
set2 = {20, 30, 40}
print(set1 ^ set2)