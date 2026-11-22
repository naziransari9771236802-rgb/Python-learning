# function arguments_______
def student(name, age):
    print("My name is:", name)
    print("My age is", age)

student("Nazir", 21)


# Positional Arguments______

def student(name, age):
    print(name)
    print(age)

student("Nazir", 21)



# practice _____
def student(name, age, city):
    print("My name is", name)
    print("My age is", age)
    print("I live in", city)

student("Nazir", 21, "Lucknow")



# Shopping_bill_______
def shopping_bill(customer_name, shirt_price, jeans_price, shoes_price):

    total = shirt_price + jeans_price + shoes_price

    discount = total * 10 / 100
    final_bill = total - discount
 
    print("------SHOPPING BILL-----")
    print("Customer:", customer_name)
    print("Shirt:", shirt_price)
    print("jeans:", jeans_price)
    print("Shoes:", shoes_price)
    print("------------------------")

    print("Total Bill: ₹", total)
    print("Discount: ₹", discount)
    print("Final Bill: ₹", final_bill)
shopping_bill("Nazir", 800, 1200, 2000)



