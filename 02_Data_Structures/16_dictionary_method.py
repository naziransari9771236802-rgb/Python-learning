# keys()________
# student = {
#     "name": "Nazir",
#     "age": 21,
#     "course": "BCA",
#     "city": "Lucknow"
# }
# print(student.keys())


# values()_____
# products = {
#     "Laptop": 450000,
#     "Mobile": 200000,
#     "Keyboard": 1000,
#     "Mouse": 500
# }
# print(products.values())


# items()___________
# employees = {
#     101: "Rahul",
#     102: "Aman",
#     103: "Nazir"
# }
# print(employees.items())



# get()_____
# user = {
#     "name": "Nazir",
#     "email": "nazir@gmail.com",
#     "city": "kushinagar"
# }
# print(user.get("email"))
# print(user.get("phone", "Not Available"))


# update()_____
# cart = {
#     "Laptop": 1,
#     "Mouse": 2,
#     "keyboard": 1
# }
# cart.update({"Mouse": 3})
# print(cart)



# pop()__________
# inventory = {
#     "Laptop": 10,
#     "Mobile": 20,
#     "Mouse": 50
# }
# removed = inventory.pop("Mouse")
# print("Removed stock:", removed)
# print("Remaining:", inventory)



# popitem()________
# orders = {
#     101: "Laptop",
#     102: "Mobile",
#     103: "Keyboard"
# }
# removed_order = orders.popitem()

# print("Removed Order:", removed_order)
# print('Remaining Orders:', orders)



# clear()________
# user_session = {
#     "username": "Nazir",
#     "login": True,
#     "role": "student"
#     }
# user_session.clear()
# print(user_session)

# print(user_session.clear())  #None



# copy()_________
# student = {
#     "name": "Nazir",
#     "age": 21,
#     "course": "BCA"
# }
# backup = student.copy()
# backup["age"] = 22
# print("original:", student)
# print("Backup:", backup)



# setdefault()___________
# settings = {
#     "username": "Nazir",
#     "theme": "Dark"
# }
# settings.setdefault("language", "English")
# print(settings)



# fromkeys()______
# subjects = ("Python", "Java", "SQL", "HTML")
# marks = dict.fromkeys(subjects, 0)

# print(marks)