
# 1. count()_________
numbers = (10, 20, 10, 50, 10)
print(numbers.count(10))

# 2.index()______
numbers = (10, 20, 30, 40)
print(numbers.index(30))

# 3. len()
numbers = (10, 20, 30, 40)
print(len(numbers))


# Slicing____________
numbers = (10, 20, 30, 40, 50)
print(numbers[1:4])


# Negative indexing_________
numbers = (10, 20, 30, 40, 50)
print(numbers[-1])
print(numbers[-2])


# Minimumm (min())_________
numbers = (45, 12, 89, 23, 67)
print(min(numbers))


# Maximum (max())_______________
numbers = (45, 12, 89, 23, 67)
print(max(numbers))


# sum(sum())___________
numbers = (10, 20, 30, 40)
print(sum(numbers))



# 4. tuple me loop__________
fruits = ("Apple", "Banana", "Mango")

for fruit in fruits:
    print(fruit)


# single element tuple______
numbers = (10,)
print(type(numbers))


# Tuple Packing and Unpacking_____
student = ("Nazir", 21, "BCA")

name, age, course = student

print(name)
print(age)
print(course)



# Concatenation(+)_________
a = (10, 20, 30)
b = (40, 50, 60)
result = a + b
print(result)



# Repetition(*)______________
numbers = (10, 20, 30)
print(numbers * 3)


# Membership(in)__________
subjects = ("HTML", "CSS", "Python", "Javascript")
print("CSS" in subjects)



# Not in_________
numbers = (10, 20, 30, 40)
print(50 not in numbers)





# Practice____________
# 1.
fruits = ("Apple", "Banana", "Mango", "Grapes", "Litchi")
print(fruits)

# 2.
numbers = (10, 20, 30, 40, 50)

print(numbers.index(20))
print(numbers.index(50))


# 3.
numbers = (10, 20, 30, 20, 40, 20)
print(numbers.count(20))


# 4.
student = ("Nazir", 21, "BCA")
name, age, course = student

print(name)
print(age)
print(course)


# 5.
subjects = ("HTML", "CSS", "Python", "JavaScript")
print("Python" in subjects)

if "Python" in subjects:
    print("Java is available")
else: 
    print("Java is not available")    
