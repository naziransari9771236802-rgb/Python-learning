# Age Checking_______
age = 21
has_id = True

if age >= 18:
    if has_id:
        print("You can enter.")
    else:
        print("ID is required.")
else:
    print("You are underage.")



# Login System()____
username = "nazir"
password = "12345"

if username == "nazir":
    if password == "12345":
        print("Login Successful!")
    else:
        print("Incorrect password!")
else:
    print("Username not found!")




# Exam result_______

marks = 86

if marks >= 33:
    print("You are Pass.")

    if marks >= 75:
        print("You are Distinction.")
    else:
        print("You passed but no distinction.")

else:
    print("You are Fail.")





# Shopping Discount________
amount = 2500
is_member = True

if amount >= 2000:
    if is_member:
        print("You got 20% discount.")
    else:
        print("You got 10% discount.")

else:
    print("No discount available.")




# Number Checking____
num = 10

if num >= 0:

    if num == 0:
        print("Number is Zero.")
    else:
        if num % 2 == 0:
            print("Positive Even Number!")
        else:
            print("Positive Odd Number!")

else:
    print("Negetive Number")