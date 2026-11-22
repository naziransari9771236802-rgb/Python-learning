def student(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)

student(name="Nazir", age=21, course="Python")


# emplyee inf0_________
def employee(name, salary, department):

    print("Name:", name)
    print("Salary:", salary)
    print("department:", department)

employee(name="Salman", salary=25000, department="IT")


# booking ticket_______
def book_ticket(customer_name, ticket_price, number_of_tickets):
    total = ticket_price * number_of_tickets

    print("Customer name:", customer_name)
    print("Ticket price:", ticket_price)
    print("Number of ticket:", number_of_tickets)
    print("Total Price:", total)

book_ticket(customer_name="Nazir", ticket_price=250, number_of_tickets=3)


# salary calculate___________
def calculate_salary(name, basic_salary, bonus, deductions):
    final_salary = basic_salary + bonus - deductions

    print("Name:", name)
    print("Basic Salary:", basic_salary)
    print("Bonus:", bonus)
    print("Deductions:", deductions)
    print("Final Salary:", final_salary)

calculate_salary(name="Nazir", basic_salary=20000, bonus=3000, deductions=1000)



# order details_________
def order_details(customer, product, price, quantity):
    total_bill = price * quantity

    print("Customer:", customer)
    print("Product:", product)
    print("price:", price)
    print("Quantity:", quantity)
    print("Total Bill:", total_bill)

    if total_bill > 50000:
        print("Premium Order")
    else:
        print("Regular Order")

order_details(
    customer="Nazir",
    product="Laptop",
    price=45000,
    quantity=2
)



# student result_____
def student_result(name, hindi, english, python):
    total = hindi + english + python
    percentage = total / 300 * 100

    print("Name:", name)
    print("Hindi:", hindi)
    print("English:", english)
    print("Python:", python)
    print("Total:", total)
    print("Percentage:", percentage)

    if percentage >= 40:
        print("Pass")
    else:
        print("Fail")

student_result(
    name="Nazir",
    hindi=75,
    english=80,
    python=90
)
