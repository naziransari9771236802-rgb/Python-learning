'''
# 1. append()
numbers = [10, 20, 30]
numbers.append(40)
print(numbers)

# 2. insert()
numbers = [10, 20, 30]
numbers.insert(1, 15)
print(numbers)

# 3. remove()
numbers = [10, 20, 30]
numbers.remove(20)
print(numbers)

# 4. pop()
numbers = [10, 20, 30]
numbers.pop()
print(numbers)

# 5. sort()
numbers = [40, 10, 30, 20]
numbers.sort()
print(numbers)

# 6. reverse()
numbers = [10, 20, 30]
numbers.reverse()
print(numbers)

# 7. count()
numbers = [10, 20, 30, 40, 10 , 20, 10]
print(numbers.count(10))

# 8. index()
fruits = ["Apple", "Banana", "Mongo"]
print(fruits.index("Mongo"))

# 9. list slicing
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4]) #list[start : end]

# 10. list ki length
fruits = ["Apple", "Banana", "Mongo"]
print(len(fruits))

# 11. list main loop
fruits = ["Apple", "Banana", "Mongo"]
for fruit in fruits:
    print(fruit)



# practice___________
# 1.
numbers = [10, 20, 30, 40, 50]
print(numbers[1])

# 2.
numbers = [10, 20, 30, 40, 50]
numbers.append(60)
print(numbers)

# 3.
numbers = [10, 20, 30, 40, 50]
numbers.remove(30)
print(numbers)

# 4.
numbers = [10, 30, 50, 30, 40]
numbers.sort()
print(numbers)
'''



# list comprehension ____________
# numbers = []

# for i in range(1, 6):
#     numbers.append(i)

#     print(numbers)



# numbers = [i for i in range(1, 6)]
# print(numbers)


# squares = [x*x for x in range(1, 6)]
# print(squares)



# list comperehension with if condition
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even = [x for x in numbers if x % 2 == 0]
# print(even)



# list comprehension with if-Else
# numbers = [1, 2, 3, 4, 5]
# result = ["Even" if x % 2 == 0 else "odd" for x in numbers]
# print(result)



# list ke sath list comprehension____________
# names = ["nazir", "rahul", "aman"]
# upper_names = [name.upper() for name in names]
# print(upper_names)


# practice___________
# 1.
# numbers = [i for i in range (1, 11)]
# print(numbers)


# 2. 
# numbers = [1, 2, 3, 4, 5, 6]
# sqaures = [x**2 for x in numbers]
# print(sqaures)


# 3. 
# numbers = [10, 15, 20, 25, 30, 35, 40]
# odd = [x for x in numbers if x % 2!= 0]
# print(odd)

# 4. 
# numbers = [1, 2, 3, 4, 5]
# multiply = [x*10 for x in numbers]
# print(multiply)

# 5.
# numbers = [11, 12, 13, 14, 15, 16]
# result = ["Even" if x % 2 == 0 else "Odd" for x in numbers]
# print(result)