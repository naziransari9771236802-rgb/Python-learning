# 1. add()______New element add karna.
fruits = {"Apple", "Mango", "Banana"}
fruits.add("Orange")
print(fruits)


# 2. update()______Multiple elements add karna.
fruits = {"Apple", "Mango", "Banana"}
fruits.update(["Grapes", "Kiwi"])
print(fruits)


# 3. remove()_______Element remove karna (Error if not found).
fruits = {"Apple", "Mango", "Banana"}
fruits.remove("Mango")
print(fruits)


# 4. discard()_____________Element remove karna (No Error if not found).
fruits = {"Apple", "Mango", "Banana"}
fruits.discard("Apple")
print(fruits)


# 5. pop()_________Random element remove karna.
numbers = {10, 20, 30, 40}
result = numbers.pop()
print("Removed:", result)
print("Remaining", numbers)


# clear()_______All elements remove karna.
numbers = {10, 20, 30, 40}
numbers.clear()
print(numbers)


# copy()______________Set ki copy banana.
original = {10, 20, 30}
new_set = original.copy()
new_set.add(40)

print("Original:", original)
print("New Set:", new_set)


# Mathematical set methods________________
# union()___Two sets combine karna.
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}
result = a.union(b)
print(result)


# intersection()________Common elements find karna.
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}
result = a.intersection(b)
print(result)



# difference()___________First set ke different elements find karna.
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}

result = a.difference(b)
print(result)
print(b.difference(a))


# symmetric_difference()_________Both sets ke non-common elements find karna.
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}
result = a.symmetric_difference(b)
print(result)



# Update Methods()____________
# intersection_update()______Only common elements keep karna.
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}

a.intersection_update(b)
print(a)



# difference_update()________Common elements remove karna.
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}
a.difference_update(b)
print(a)



# symmetric_difference_update()________Only non-common elements keep karna.
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}
a.symmetric_difference_update(b)
print(a)



# Comparison methods__________
# issubset()_____Subset check karna.
a = {10, 20}
b = {10, 20, 30, 40, 50}
result = a.issubset(b)
print(result)



# issuperset()____________Superset check karna.
a = {10, 20, 30, 40, 50}
b = {10, 20}
result = a.issuperset(b)
print(result)



# isdisjoint()_________No common elements check karna.
a = {10, 20, 30}
b = {40, 50, 60}
result = a.isdisjoint(b)
print(result)