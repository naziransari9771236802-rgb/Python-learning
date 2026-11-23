#______________________ *args__________________

def add_numbers(*args):
    print(args)
add_numbers(10, 20, 30)


# calculate _________
def calculate_total(*args):
    total = 0

    for number in args:
        total += number

    print("Total:", total)

calculate_total(10, 20, 30, 40)



# Student marks____________
def student_marks(*args):
    total = 0

    for number in args:
        total += number

    print("Total:", total)

student_marks(80, 75, 90, 85)



# longest number find krna__________
def find_max(*args):
    longest_number = args[0]

    for number in args:
        if number > longest_number:
            longest_number = number

    print("Maximum Number:", longest_number)

find_max(12, 45, 78, 23, 90, 34)



# find Minimum Number
def find_min(*args):
    minimum_number = args[0]

    for number in args:
        if number < minimum_number:
            minimum_number = number

    print("Minimun Number:", minimum_number)
find_min(12, 45, 78, 23, 5, 34)




# Calculate Average_________
def calculate_average(*args):
    total = 0

    for number in args:
        total += number

    average = total / len(args)

    print("Total:", total)
    print("Average:", average)

calculate_average(10, 20, 30, 40, 50)



# number count_______
def number_count(*args):
    positive = 0
    negative = 0
    zeros = 0

    for number in args:
        if number > 0:
            positive += 1

        elif number < 0:
            negative += 1

        else:
            zeros += 1

    print("Total Number:", len(args))
    print("Postive Number:", positive)
    print("Negative Number:", negative)
    print("zeros:", zeros)

number_count(10, -5, 0, 20, -8, 0, 15)



# __________________________**kwargs_____________________

def student_details(**kwargs):
    print(kwargs)

student_details(name="Nazir", age=21, course="BCA")



# Dictionary ki trh access krna_______
def student_details(**kwargs):
    print("Name:", kwargs["name"])
    print("Age:", kwargs["age"])
    print("Course:", kwargs["course"])

student_details(name="sahjad", age=21, course="BCA")



# **kwargs me loop________
def student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student_details(name="Nazir", age=21, course="BCA")



# emplyee_details______
def emplyee_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

emplyee_details(name="Nazir", age=21, department="IT", salary=25000)




# Easy-Medium______
def calculate_total(**kwargs):
    total = 0

    for key, value in kwargs.items():
        total += value
  
    print("Total Amount:", total)

calculate_total(
    laptop=50000,
    mouse=500,
    keyboard=1500,
    monitor=12000
)



# find Maximum________
def find_maximum(**kwargs):
    highest_marks = 0
    highest_scorer = ""

    for key, value in kwargs.items():
        if value > highest_marks:
            highest_marks = value
            highest_scorer = key

    print("Highest Scorer:", highest_scorer)
    print("Highest Marks:", highest_marks)

find_maximum(
    Rahul=85,
    Aman=92,
    Nazir=95,
    Rohit=78
)



# Filter Student______
def passed_students(**kwargs):

    print("Passed Student:")

    for key, value in kwargs.items():
        if value > 40:
            print(key, ":", value)

passed_students(
    Rahul=85,
    Aman=32,
    Nazir=95,
    Rohit=28,
    Sameer=45
)



# Calculate salary______
def calculate_salary(**kwargs):
    total = 0
    
    print("All Employee salary:")

    for key, value in kwargs.items():
        print(key, ":", value)
        total += value
    print("\nTotal salary:", total)

calculate_salary(
    Nazir=25000,
    Rahul=30000,
    Aman=20000,
    Rohit=28000
)