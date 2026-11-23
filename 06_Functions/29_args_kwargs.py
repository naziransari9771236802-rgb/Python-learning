# *args______
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
# def find_max(*args):
#     longest_number = args[0]

#     for number in args:
#         if number > longest_number:
#             longest_number = number

#     print("Maximum Number:", longest_number)

# find_max(12, 45, 78, 23, 90, 34)



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