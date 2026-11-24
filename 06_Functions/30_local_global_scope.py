# ________________LOCAL SCOPE_____________
# def student():
#     name = "Nazir"
#     print("Student Name:", name)
# student()

# Practice _______
# def student():
#     name = "Nazir"

# student()
# print(name) #nameError: name 'name' is not defined


# def employee():
#     name = "Rahul"
#     salary = 25000
#     print("Employee name:", name)
#     print("Salary:", salary)
# employee()



# def student():
#     age = 21
#     print("Inside Function:", age)

# student()
# student()



# def calculate():
#     number = 10
#     number = number + 5
#     print(number)
# calculate()




# def first():
#     name = "Nazir"
#     print(name)

# def second():
#     print(name)  # NameError: name 'name' is not defined

# first()
# second()



# _________________GLOBAL________________
name = "Nazir"

def student():
    print(name)

student()

print(name)



# Practice________
name = "Nazir"

def student():
    print("Student Name:", name)

student()



# college student _______
college = "ABC College"

def student1():
    name = "Nazir"
    print(name, "studies in", college)

def student2():
    name = "Rahul"
    print(name, "studies in", college)

student1()
student2()



# Bank Account Balance_________
balance = 5000

def deposit():
    global balance
    balance = balance + 2000
    print("After Deposite:", balance)

def withdraw():
    global balance
    balance = balance - 1000
    print("After Withdrawl:", balance)

deposit()
withdraw()

print("Final Balance:", balance)



# Online Shopping Cart_________
cart_total = 1000

def add_product():
    global cart_total
    cart_total += 500

def apply_discount():
    global cart_total
    cart_total -= 200

add_product()
apply_discount()

print("Final Cart Amount:", cart_total)


# school list__________
total_student = 500

def add_student():
    global total_student
    total_student = total_student + 50
    print("After Admission:", total_student)

def leave_student():
    global total_student
    total_student = total_student - 20
    print("After Leaving:", total_student)

add_student()
leave_student()

print("Total Student:", total_student)