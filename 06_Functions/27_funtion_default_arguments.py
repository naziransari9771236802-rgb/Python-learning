# shopping_bill________
def shopping_bill(customer_name, shirt_price, jeans_price, shoes_price=0):

    total = shirt_price + jeans_price + shoes_price

    print("customer:", customer_name)
    print("Total Bill:", total)

shopping_bill("Nazir", 800, 1200)




# Order_food_________
def order_food(customer_name, food_price, delivery_charge=40):
    total = food_price + delivery_charge

    print("Customer:", customer_name)
    print("food price:", food_price)
    print("Delivery Charges:", delivery_charge)
    print("Total Amount:", total)

order_food("Nazir", 200)



# Mobile recharge App________
def mobile_recharge(customer_name, recharge_amount, processing_fee=5):

    total = recharge_amount + processing_fee

    print("Customer name:", customer_name)
    print("Recharge amount:", recharge_amount)
    print("Processing fee:", processing_fee)
    print("Total payment:", total)

mobile_recharge("sahjad", 299)



# Movie Ticket Booking 🎬
def book_ticket(customer_name, ticket_price, number_of_ticket=1):

    total = ticket_price * number_of_ticket

    print("Customer name:", customer_name)
    print("Ticket Price:", ticket_price)
    print("Number of ticket:", number_of_ticket)
    print("Total:", total)

book_ticket("Nazir", 150, 3)